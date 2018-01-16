from selenium.webdriver.support.wait import (
    TimeoutException,
    WebDriverWait,
)


class MyAccountPage(object):
    # model of the header at the top of each page
    wait_timeout = 5

    def __init__(self, browser):
        self.browser = browser

    def wait_until_loaded(self):
        """Determines if the page is ready by checking if the order history button is displayed"""
        try:
            WebDriverWait(self.browser, self.wait_timeout).until(
                lambda d: self.order_history_and_details_button.is_displayed())
        except TimeoutException:
            try:
                self.browser.refresh()
                WebDriverWait(self.browser, self.wait_timeout).until(
                    lambda d: self.order_history_and_details_button.is_displayed())
            except TimeoutException:
                return TimeoutException

    @property
    def order_history_and_details_button(self):
        # the order history and details button
        return self.browser.find_element_by_css_selector(".icon-list-ol+ span")
