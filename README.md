# SCSeleniumTest
Set up a test framework and get some tests running


## Development setup
I'm working on MacOS, with my preferred language Python(v2.7).

To set up a virtual environment I used virtualenvwrapper:
https://virtualenvwrapper.readthedocs.io/en/latest/

In my virtual environments I installed the pytest framework:

'$ pip install -U pytest'

Install selenium:

'$ pip install selenium'

Install the pytest-selenium plugin:

'$ pip install pytest-selenium'

I'm running my tests in Chrome so Chrome webdriver is required:

'$ pip install chromedriver'


## Running tests
To run a each test, with the html report enabled:
'$ pytest -v -k test_purchase_two_items --html=report.html'
'$ pytest -v -k test_review_order --html=report.html'
'$ pytest -v -k test_capture_image --html=report.html'

Note - remove ' --html=report.html' to run each test without report being generated.


## Reports
I've named the reports report.html. This will save in the local repository directory.
