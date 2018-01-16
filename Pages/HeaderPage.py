from selenium.webdriver.support.wait import (
    TimeoutException,
    WebDriverWait,
)


class HeaderPage(object):
    # model of the header at the top of each page
    wait_timeout = 5

    def __init__(self, browser):
        self.browser = browser

    def wait_until_loaded(self):
        """Determines if the page is ready by checking if the search box is displayed"""
        try:
            WebDriverWait(self.browser, self.wait_timeout).until(lambda d: self.search_box.is_displayed())
        except TimeoutException:
            try:
                self.browser.refresh()
                WebDriverWait(self.browser, self.wait_timeout).until(lambda d: self.search_box.is_displayed())
            except TimeoutException:
                return TimeoutException

    @property
    def search_box(self):
        # search box
        return self.browser.find_element_by_id("search_query_top")

    def search(self, item):
        # search for an item
        self.search_box.send_keys(item)
        self.search_box.send_keys('\n')

    def clear_search_box(self):
        # clear any text currently in the search box
        self.search_box.clear()

    @property
    def shopping_cart(self):
        # link to open the shopping cart
        return self.browser.find_element_by_css_selector(".shopping_cart > a")

    @property
    def shopping_cart_check_out(self):
        # link to check out within the shopping cart pop up
        return self.browser.find_element_by_css_selector("#button_order_cart span")
