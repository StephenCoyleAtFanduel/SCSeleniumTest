from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.MyAccountPage import MyAccountPage
from Pages.OrderHistoryPage import OrderHistoryPage


def test_capture_image(browser, resource):
    """
    insert an assert which will fail and capture a screen-grab when it does
    NOTE - to generate report please add --html=report.html at the end of test name,
    e.g.:
    pytest -v -k test_capture_image --html=report.html
    this should create report.html in the repository directory
    """
    browser.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

    lp = LoginPage(browser)
    lp.login_stephen()

    # click on the orders history button
    map = MyAccountPage(browser)
    map.order_history_and_details_button.click()

    ohp = OrderHistoryPage(browser)
    # FAILING ASSERT - confirm that the 1st order number in the table = "ABCDEFG"
    assert ohp.order_history_table_first_entry.text == "ABCDEFG"

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

    browser.quit()
