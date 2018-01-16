import re
from selenium.webdriver.support.wait import (
    TimeoutException,
    WebDriverWait,
)


class ShoppingCartPage(object):
    # model of the header at the top of each page
    wait_timeout = 5

    def __init__(self, browser):
        self.browser = browser

    def wait_until_loaded(self):
        """Determines if the page is ready by checking if the first product's colour and size is displayed"""
        try:
            WebDriverWait(self.browser, self.wait_timeout).until(
                lambda d: self.first_product_colour_and_size.is_displayed())
        except TimeoutException:
            try:
                self.browser.refresh()
                WebDriverWait(self.browser, self.wait_timeout).until(
                    lambda d: self.first_product_colour_and_size.is_displayed())
            except TimeoutException:
                return TimeoutException

    @property
    def first_product_colour_and_size(self):
        # first product colour & size
        return self.browser.find_element_by_css_selector(".odd small a")

    @property
    def second_product_colour_and_size(self):
        # second product colour & size
        return self.browser.find_element_by_css_selector(".even small a")

    @property
    def first_product_total_price(self):
        # first product total price
        return self.browser.find_element_by_css_selector(".odd .cart_total .price")

    @property
    def second_product_total_price(self):
        # second product total price
        return self.browser.find_element_by_css_selector(".even .cart_total .price")

    @property
    def total_products_price(self):
        # total products price
        return self.browser.find_element_by_id("total_product")

    @property
    def total_shipping_price(self):
        # total shipping price
        return self.browser.find_element_by_id("total_shipping")

    @property
    def grand_total_price(self):
        # grand total of products + shipping + any other costs
        return self.browser.find_element_by_id("total_price")

    @property
    def proceed_to_checkout_button(self):
        # proceed to checkout button
        return self.browser.find_element_by_css_selector(".button.btn.btn-default.standard-checkout.button-medium")

    def price_convert(self, currency):
        # trim currency identifier out of prices so we can add them together
        trim = re.compile(r'[^\d.,]+')
        number = trim.sub('', currency)
        return number
