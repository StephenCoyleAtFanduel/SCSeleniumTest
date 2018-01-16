import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from selenium.webdriver.common.keys import Keys
driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    #Extends the pytest Plugin to take and embed a screenshot in the html report whenever test fails.

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot"style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'% file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver

@pytest.fixture()
def resource():
    print("setup")
    yield "resource"
    print("teardown")

@classmethod
def setup_class(cls):
    "Runs once per class"

@classmethod
def teardown_class(cls):
    "Runs at end of class"
