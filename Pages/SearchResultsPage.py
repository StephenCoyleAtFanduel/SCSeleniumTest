from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import (
    TimeoutException,
    WebDriverWait,
)
from selenium.common.exceptions import StaleElementReferenceException


class SearchResultsPage(object):
    # model of the My Account page
    wait_timeout = 5

    def __init__(self, browser):
        self.browser = browser

    def wait_until_loaded(self):
        """Determines if the page is ready by checking if the product in stock icon is displayed"""
        try:
            WebDriverWait(self.browser, self.wait_timeout).until(lambda d: self.product_in_stock.is_displayed())
        except TimeoutException:
            try:
                self.browser.refresh()
                WebDriverWait(self.browser, self.wait_timeout).until(lambda d: self.product_in_stock.is_displayed())
            except TimeoutException:
                return TimeoutException

    def wait_for_added_to_cart_confirmation(self):
        """Wait for added to cart confirmation text"""
        wait = WebDriverWait(self.browser, self.wait_timeout, ignored_exceptions=StaleElementReferenceException)
        wait.until(lambda d: self.added_to_cart_confirmation.is_displayed())

    @property
    def product_in_stock(self):
        # product in stock icon
        return self.browser.find_element_by_css_selector(".available-now")

    @property
    def quick_view(self):
        # quick view icon, only available when mouse is hovered over item
        return self.browser.find_element_by_class_name("quick-view")

    @property
    def qv_size_menu(self):
        # the size menu in the quick view pop up
        return self.browser.find_element_by_id("uniform-group_1")

    def qv_select_size_large(self):
        # select size L in the qv size dropdown
        mySelect = Select(self.browser.find_element_by_id("group_1"))
        mySelect.select_by_visible_text("L")

    @property
    def qv_plus_icon(self):
        # the size menu in the quick view pop up
        self.browser.switch_to_frame(self.browser.find_element_by_class_name('fancybox-iframe'))
        return self.browser.find_element_by_class_name("icon-plus")

    @property
    def qv_add_to_cart_button(self):
        # the add to cart button in the quick view
        return self.browser.find_element_by_id("add_to_cart")

    @property
    def added_to_cart_confirmation(self):
        # the left pane of the confirmation pop up which confirms an item has been added to cart
        return self.browser.find_element_by_css_selector(".layer_cart_product h2")

    @property
    def continue_shopping_button(self):
        # the continue shopping button in the added to cart confirmation pop up
        return self.browser.find_element_by_css_selector(".exclusive-medium span")

    @property
    def close_confirmation_pop_up(self):
        # the continue shopping button in the added to cart confirmation pop up
        return self.browser.find_element_by_css_selector(".cross")

    @property
    def proceed_to_checkout_button(self):
        # the continue shopping button in the added to cart confirmation pop up
        return self.browser.find_element_by_class_name("btn btn-default button button-medium")
