from selenium.webdriver.support.wait import (
    TimeoutException,
    WebDriverWait,
)
email_address = "stephen.coyle@test.com"
user_password = "BJSSTest"


class LoginPage(object):
    # model of the login page
    wait_timeout = 5

    def __init__(self, browser):
        self.browser = browser

    def wait_until_loaded(self):
        """Determines if the page is ready by checking if the email field is displayed"""
        try:
            WebDriverWait(self.browser, self.wait_timeout).until(lambda d: self.email.is_displayed())
        except TimeoutException:
            try:
                self.browser.refresh()
                WebDriverWait(self.browser, self.wait_timeout).until(lambda d: self.email.is_displayed())
            except TimeoutException:
                return TimeoutException

    @property
    def email(self):
        # email field
        return self.browser.find_element_by_id("email")

    @property
    def password(self):
        # password field
        return self.browser.find_element_by_id("passwd")

    @property
    def submit(self):
        # Submit button
        return self.browser.find_element_by_id("SubmitLogin")

    def login_stephen(self):
        # login as pre-created user Stephen
        self.email.send_keys(email_address)
        self.password.send_keys(user_password)
        self.submit.click()
