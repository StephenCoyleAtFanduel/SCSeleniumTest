from selenium.webdriver.support.wait import (
    TimeoutException,
    WebDriverWait,
)


class ShippingPage(object):
    # model of the header at the top of each page
    wait_timeout = 5

    def __init__(self, browser):
        self.browser = browser

    def wait_until_loaded(self):
        """Determines if the page is ready by checking if the terms of service checkbox is displayed"""
        try:
            WebDriverWait(self.browser, self.wait_timeout).until(
                lambda d: self.terms_of_service_checkbox.is_displayed())
        except TimeoutException:
            try:
                self.browser.refresh()
                WebDriverWait(self.browser, self.wait_timeout).until(
                    lambda d: self.terms_of_service_checkbox.is_displayed())
            except TimeoutException:
                return TimeoutException

    @property
    def terms_of_service_checkbox(self):
        # the checkbox for agreeing to terms of service
        return self.browser.find_element_by_id("cgv")

    @property
    def proceed_to_checkout_button(self):
        # proceed to checkout button
        return self.browser.find_element_by_css_selector(".button.btn.btn-default.standard-checkout.button-medium")
