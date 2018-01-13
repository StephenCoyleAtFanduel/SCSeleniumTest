# SCSeleniumTest
Set up a test framework and get some tests running


## Development setup
I'm working on MacOS, with my preferred language Python(v2.7).

To set up a virtual environment I used virtualenvwrapper:
https://virtualenvwrapper.readthedocs.io/en/latest/

In my virtual environments I installed the pytest framework:

'$ pip install -U pytest'

Install the pytest-selenium plugin:

'$ pip install pytest-selenium'

I'm running my tests in Chrome so Chrome webdriver is required:

'$ pip install chromedriver'


## Running tests
To run all tests:

'$ make tests threads="number of threads"'

To run a subset of the tests:

'$ pytest -v -k PATTERN'
