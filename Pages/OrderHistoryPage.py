from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import (
    TimeoutException,
    WebDriverWait,
)
from selenium.common.exceptions import StaleElementReferenceException


class OrderHistoryPage(object):
    # model of the header at the top of each page
    wait_timeout = 5

    def __init__(self, browser):
        self.browser = browser

    def wait_until_loaded(self):
        """Determines if the page is ready by checking if the order history table's first entry is displayed"""
        try:
            WebDriverWait(self.browser, self.wait_timeout).until(
                lambda d: self.order_history_table_first_entry.is_displayed())
        except TimeoutException:
            try:
                self.browser.refresh()
                WebDriverWait(self.browser, self.wait_timeout).until(
                    lambda d: self.order_history_table_first_entry.is_displayed())
            except TimeoutException:
                return TimeoutException

    def wait_for_add_message_choose_product(self):
        """Wait for the product dropdown list to display"""
        wait = WebDriverWait(self.browser, self.wait_timeout, ignored_exceptions=StaleElementReferenceException)
        wait.until(lambda d: self.add_message_choose_product.is_displayed())

    def wait_for_message_successful_confirmation(self):
        """Wait for the 'Message successfully sent' confirmation bar to display"""
        wait = WebDriverWait(self.browser, self.wait_timeout, ignored_exceptions=StaleElementReferenceException)
        wait.until(lambda d: self.message_successful_confirmation.is_displayed())

    @property
    def order_history_table_first_entry(self):
        # the 1st entry in the order history table
        return self.browser.find_element_by_css_selector(".first_item .color-myaccount")

    @property
    def add_message_choose_product(self):
        # the product dropdown list when adding a message
        return self.browser.find_element_by_css_selector("select.form-control")

    def choose_product_select_blouse(self):
        # select the blouse in the product dropdown
        mySelect = Select(self.add_message_choose_product)
        mySelect.select_by_visible_text("Blouse - Color : Black, Size : S")

    @property
    def message_box(self):
        # the message box for leaving an order comment
        return self.browser.find_element_by_css_selector("textarea.form-control")

    @property
    def send_button(self):
        # the send comments button
        return self.browser.find_element_by_css_selector("button.btn.btn-default.button-medium")

    @property
    def message_successful_confirmation(self):
        # the 'Message successfully sent' confirmation bar
        return self.browser.find_element_by_css_selector("p.alert.alert-success")

    @property
    def message_history(self):
        # the message history top entry
        return self.browser.find_element_by_xpath('//*[@id="block-order-detail"]/div[5]/table/tbody/tr[1]/td[2]')
