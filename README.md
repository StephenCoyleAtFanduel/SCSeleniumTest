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
To run each test, with the html report enabled:
'$ pytest -v -k test_purchase_two_items --html=report.html'
'$ pytest -v -k test_review_order --html=report.html'
'$ pytest -v -k test_capture_image --html=report.html'

Note - remove ' --html=report.html' to run each test without report being generated.


## Reports
Running the test as above will name the reports report.html and will create them in the local repository directory.


## Tech Debt
Some updates I would like to do if I had more time (in no particular order):
- Speed up login process for each test by adding a fixture that would log user in via the API (inject  x-auth-token).
Once the login has been tested once it seems unnecessary/slow to repeatedly test it at the start of every other test.
 
- Add more fixtures & plugins to conftest.py, or configure conftest.py to import fixtures from elsewhere to make the
directories easier to navigate.
 
- Have a random user set up for every test (don't store username & pwd in the code).

- Create a fixture for logging in.

- Handle exceptions, e.g. out of stock.

- Create a fixture for opening quick view (save repeating the mouse over code).

- I've not taken into account that the particular products I've searched for/bought could be removed from sale,
marked as out of stock, change name, similar items added, etc.

- If I worked on a website like this I would ask to add test hooks.

- Add in setup & tear down.

- Look for an alternative to the find_element_by_xpath that I used for 1 element as there was no id and the css wasn't
unique. I should really be using the order reference.

- Add in more asserts, e.g. store order number and assert we review the correct order.

- Get the screenshot on fail to take a screenshot of the whole page (not just what's in view).

- Add the test name, date and time to the generated report file name.

- Reports and screenshots should be available with the pytest-selenium plugin
 (http://pytest-selenium.readthedocs.io/en/latest/user_guide.html#html-report) but I couldn't get the screenshot to
 display in the report. Further investigation required as this would be a lot simpler than the method I've used
 through the pytest-html plugin.

- test_purchase_two_items feels too big for 1 test, would like to split this into 2 or more, within the class.


## pip list of my venv in case of problems
attrs (17.4.0)
certifi (2017.11.5)
chardet (3.0.4)
chromedriver (2.24.1)
funcsigs (1.0.2)
idna (2.6)
pip (9.0.1)
pluggy (0.6.0)
py (1.5.2)
pytest (3.3.2)
pytest-base-url (1.4.1)
pytest-html (1.16.1)
pytest-metadata (1.5.1)
pytest-selenium (1.11.4)
pytest-variables (1.7.0)
requests (2.18.4)
selenium (3.8.1)
setuptools (38.4.0)
six (1.11.0)
urllib3 (1.22)
wheel (0.30.0)