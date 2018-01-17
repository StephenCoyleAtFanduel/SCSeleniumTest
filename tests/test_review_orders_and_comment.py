from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.MyAccountPage import MyAccountPage
from Pages.OrderHistoryPage import OrderHistoryPage
from Pages.HeaderPage import HeaderPage


def test_review_order(browser):
    """
    Review previous order and add a message
    """
    browser.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

    lp = LoginPage(browser)
    lp.login_stephen()

    # click on the orders history button
    map = MyAccountPage(browser)
    map.order_history_and_details_button.click()

    # Open the latest (top) item in the order history
    ohp = OrderHistoryPage(browser)
    ohp.order_history_table_first_entry.click()

    # wait for the add message product select dropdown list to display before proceeding
    ohp.wait_for_add_message_choose_product()

    # select a product to comment on
    ohp.choose_product_select_blouse()

    # enter a comment
    comment = "This is a test comment"
    ohp.message_box.send_keys(comment)

    # submit comment
    ohp.send_button.click()

    # wait for the 'Message successfully sent' confirmation bar to display before proceeding
    ohp.wait_for_message_successful_confirmation()
    assert ohp.message_successful_confirmation.is_displayed()

    # confirm that comment is now logged in message history
    assert ohp.message_history.text == comment

    hp = HeaderPage(browser)
    hp.logout.click()
    browser.quit()
