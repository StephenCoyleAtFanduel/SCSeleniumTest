import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Pages.LoginPage import LoginPage
from Pages.HeaderPage import HeaderPage
from Pages.SearchResultsPage import SearchResultsPage
from Pages.ShoppingCartPage import ShoppingCartPage
from Pages.AddressesPage import AddressesPage
from Pages.ShippingPage import ShippingPage
from Pages.PaymentPage import PaymentPage
from selenium.webdriver.common.action_chains import ActionChains
from decimal import *


def test_purchase_two_items(browser):
    """
    Happy path, purchase 2 items
    """
    browser.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

    lp = LoginPage(browser)
    lp.login_stephen()

    # search for an item
    item = "Faded Short Sleeve T-shirts"
    hp = HeaderPage(browser)
    hp.search(item)

    # on the search results open quick view for item
    srp = SearchResultsPage(browser)
    assert srp.product_in_stock.is_displayed() is True  # confirm the item is in stock
    actions = ActionChains(browser)  # quick view only available on mouse over
    actions.move_to_element(srp.product_in_stock).perform()  # this moves mouse to element
    srp.quick_view.click()  # now able to see/click on quick view icon

    # assert that the plus icon in the iFrame is showing - also switches to iFrame
    assert srp.qv_plus_icon.is_displayed()

    # Change the size to large
    srp.qv_select_size_large()

    # click add to cart
    srp.qv_add_to_cart_button.click()

    # wait for the added to cart confirmation text to display before proceeding
    srp.wait_for_added_to_cart_confirmation()

    # assert that the item was successfully added to cart
    assert srp.added_to_cart_confirmation.text == "Product successfully added to your shopping cart"

    # click to continue shopping
    srp.continue_shopping_button.click()

    # clear the search box
    hp.clear_search_box()

    # search for a different item
    item = "blouse"
    hp.search(item)

    # on the search results open quick view for item
    assert srp.product_in_stock.is_displayed() is True  # confirm the item is in stock
    actions = ActionChains(browser)  # quick view only available on mouse over
    actions.move_to_element(srp.product_in_stock).perform()  # this moves mouse to element
    srp.quick_view.click()  # now able to see/click on quick view icon

    # assert that the plus icon in the iFrame is showing - also switches to iFrame
    assert srp.qv_plus_icon.is_displayed()

    # click add to cart
    srp.qv_add_to_cart_button.click()

    # wait for the added to cart confirmation text to display before proceeding
    srp.wait_for_added_to_cart_confirmation()

    # assert that the item was successfully added to cart
    successful_message = "Product successfully added to your shopping cart"
    assert srp.added_to_cart_confirmation.text == successful_message

    # click to close the pop up and open the shopping cart
    srp.close_confirmation_pop_up.click()
    hp.shopping_cart.click()

    # confirm that the t-shirt is displaying the correct colour and size
    scp = ShoppingCartPage(browser)
    tshirt_expected_colour_and_size = "Color : Orange, Size : L"
    assert scp.first_product_colour_and_size.text == tshirt_expected_colour_and_size

    # confirm that the t-shirt is displaying the correct total price
    tshirt_expected_total_price = "$16.51"
    assert scp.first_product_total_price.text == tshirt_expected_total_price

    # confirm that the blouse is displaying the correct colour and size
    blouse_expected_colour_and_size = "Color : Black, Size : S"
    assert scp.second_product_colour_and_size.text == blouse_expected_colour_and_size

    # confirm that the t-shirt is displaying the correct total price
    blouse_expected_total_price = "$27.00"
    assert scp.second_product_total_price.text == blouse_expected_total_price

    # storing the grand total price text to use as a check later
    grand_total_price = scp.grand_total_price.text

    # strip out the $ from the prices so we are left with a numeric value only
    tshirt_converted_price = scp.price_convert(scp.first_product_total_price.text)
    blouse_converted_price = scp.price_convert(scp.second_product_total_price.text)
    total_products_converted_price = scp.price_convert(scp.total_products_price.text)
    total_shipping_converted_price = scp.price_convert(scp.total_shipping_price.text)
    grand_total_converted_price = scp.price_convert(scp.grand_total_price.text)

    # asserts to confirm values add up correctly
    assert Decimal(tshirt_converted_price) + Decimal(blouse_converted_price) == Decimal(total_products_converted_price)
    assert Decimal(total_products_converted_price) + Decimal(total_shipping_converted_price) == \
        Decimal(grand_total_converted_price)

    # click proceed to checkout to go to the addresses page
    scp.proceed_to_checkout_button.click()

    # click proceed to checkout to go to the shipping page
    ap = AddressesPage(browser)
    ap.proceed_to_checkout_button.click()

    # click to agree to the terms of service and proceed to the payment page
    sp = ShippingPage(browser)
    sp.terms_of_service_checkbox.click()
    sp.proceed_to_checkout_button.click()

    # click to pay by bank wire
    pp = PaymentPage(browser)
    pp.pay_by_wire_button.click()

    # check that the final order price is what we expected
    assert pp.final_payment_amount.text == grand_total_price

    # click to confirm order
    pp.confirm_order.click()

    hp.logout.click()
    browser.quit()
