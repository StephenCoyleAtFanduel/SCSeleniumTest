from selenium.webdriver.support.wait import (
    TimeoutException,
    WebDriverWait,
)


class PaymentPage(object):
    # model of the header at the top of each page
    wait_timeout = 5

    def __init__(self, browser):
        self.browser = browser

    def wait_until_loaded(self):
        """Determines if the page is ready by checking if the pay by wire button is displayed"""
        try:
            WebDriverWait(self.browser, self.wait_timeout).until(
                lambda d: self.pay_by_wire_button.is_displayed())
        except TimeoutException:
            try:
                self.browser.refresh()
                WebDriverWait(self.browser, self.wait_timeout).until(
                    lambda d: self.pay_by_wire_button.is_displayed())
            except TimeoutException:
                return TimeoutException

    @property
    def pay_by_wire_button(self):
        # proceed to checkout button
        return self.browser.find_element_by_css_selector(".bankwire")

    @property
    def final_payment_amount(self):
        # the final payment amount
        return self.browser.find_element_by_css_selector("#amount")

    @property
    def confirm_order(self):
        # confirm order button
        return self.browser.find_element_by_css_selector("#cart_navigation span")
