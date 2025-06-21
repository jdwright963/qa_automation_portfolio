# Import the pytest library, which is the testing framework being used.
import pytest

# Import all the Page Object classes that will be used in the test scenarios defined in this file.
# Each class represents a specific page of the web application and encapsulates its elements and actions.
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.confirmation_page import ConfirmationPage

# Use pytest's parametrize feature to run the following test function multiple times,
# each time with a different set of 'product_id' and 'expected_name' values.
# This allows testing the same logic (e.g., adding a product to cart and verifying its name)
# for several different products without duplicating the test code.
@pytest.mark.parametrize(
    "product_id, expected_name",
    [
        ("sauce-labs-bike-light", "Sauce Labs Bike Light"),
        ("sauce-labs-backpack",    "Sauce Labs Backpack"),
        ("sauce-labs-bolt-t-shirt", "Sauce Labs Bolt T-Shirt"),
    ],
)

# Tests logging in successfully and adding a product to the cart
def test_login_and_add_to_cart(driver, product_id, expected_name):
    
    # Create an instance of the LoginPage. The constructor loads the page.
    login = LoginPage(driver)
    
    # Login with valid credentials.
    login.login("standard_user", "secret_sauce")

    # Assert that the user is now logged in.
    # If not, fail the test with the given message.
    assert login.is_logged_in(), "Login failed: Products page not displayed"

    # Create an instance of the Products page. Add the product with product_id to the cart. 
    # Then go to the cart page.
    products = ProductsPage(driver)
    products.add_to_cart(product_id)
    cart_page = products.go_to_cart()


    # Retreive a list of all the items in the cart.
    items_in_cart = cart_page.get_cart_items()

    # Assert that the 'expected_name'is present in the 'items_in_cart' list.
    # If the 'expected_name' is not found in the list, the assertion fails,
    # and Pytest will report an AssertionError with the custom message,
    # showing what was expected versus what was actually found in the cart.
    assert expected_name in items_in_cart, f"Expected '{expected_name}' in cart, got {items_in_cart}"

# Test invalid login.
def test_invalid_login_shows_error(driver):
    login = LoginPage(driver)
    
    # Attempt to login with invalid credentials.
    login.login("bad_user", "wrong_pass")

    # Asserts that an error message is displayed on the page.
    # Otherwise, Pytest will report an AssertionError with the custom message.
    assert login.error_message_displayed(), "Error message should be displayed for invalid login"

@pytest.mark.parametrize(
    "product_id, product_name",
    [
        ("sauce-labs-backpack", "Sauce Labs Backpack"),
        ("sauce-labs-bike-light", "Sauce Labs Bike Light"),
    ],
)

# Test the addition and removal of an item from the cart.
def test_add_and_remove_item(driver, product_id, product_name):
    login = LoginPage(driver)

    # Login with valid credentials.
    login.login("standard_user", "secret_sauce")

    # Assert that the user is now logged in.
    # If not, fail the test with the given message.
    assert login.is_logged_in(), "Login failed"

    # Create an instance of the Products page. Add the product with product_id to the cart. 
    # Remove the product with the product_id. Then, go to the cart page.
    products = ProductsPage(driver)
    products.add_to_cart(product_id)
    products.remove_from_cart(product_id)
    cart_page = products.go_to_cart()

    # Retrieve a list of all item names displayed on the cart page.
    items = cart_page.get_cart_items()

    # Assert that the 'product_name' (which was previously removed) is not present in the 'items' list
    # (the current contents of the cart). This verifies that a product removal was successful.
    # Otherwise, raising an AssertionError with a message indicating the product was unexpectedly present.
    assert product_name not in items, f"Expected '{product_name}' to be removed, but found {items}"

# Self explanatory function name. Also see prior comments for identical lines of code.
def test_empty_cart_shows_no_items(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert login.is_logged_in(), "Login failed"

    products = ProductsPage(driver)

    cart_page = products.go_to_cart()
    items = cart_page.get_cart_items()

    # Assert the list of items in the cart is empty.
    assert items == [], f"Expected empty cart, but found items: {items}"

# Test that the badge on the cart icon that indicates the number of items in the
# cart updates correctly when a product is added to the cart
def test_cart_badge_updates(driver):

    # See prior comments
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert login.is_logged_in(), "Login failed"
    products = ProductsPage(driver)
    products.add_to_cart("sauce-labs-bike-light")

    # Retrieves the current count displayed on the shopping cart badge (the number of items in the cart).
    badge = products.get_cart_badge_count()

    # Assert that the count is 1 (since only 1 product was added to the cart).
    assert badge == 1, f"Expected cart badge count 1, got {badge}"

# Test that the subtotal on the overview page is correct.
def test_overview_subtotal_matches_items(driver):

    # See prior comments
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert login.is_logged_in(), "Login failed"
    products = ProductsPage(driver)

    # Add products to the cart with Prices of $29.99 and $9.99
    products.add_to_cart("sauce-labs-backpack")
    products.add_to_cart("sauce-labs-bike-light")
    cart_page = products.go_to_cart()
    
    # Retrieves a list of prices for all items currently in the cart.
    item_prices = cart_page.get_item_prices()

    # Sum the list of item prices and round to 2 decimal places to remove any float inaccuracies.
    # Then, click the checkout button to go to the checkout page.
    expected_subtotal = round(sum(item_prices), 2)
    checkout_page = cart_page.click_checkout()

    # Self explanatory
    checkout_page.enter_customer_info("Test", "User", "12345")
    overview_page = checkout_page.click_continue()

    # Retrieves the "Item total" amount (subtotal before tax).
    subtotal = overview_page.get_item_total()

    # Assert that the subtotal retrieved from the overview page is equal to the expected subtotal calculated above.
    assert round(subtotal, 2) == expected_subtotal, f"Subtotal mismatch: expected {expected_subtotal}, got {subtotal}"

# Self explanatory
def test_complete_checkout_flow(driver):

    # See prior comments.
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert login.is_logged_in(), "Login failed"

    # See prior comments.
    products = ProductsPage(driver)
    products.add_to_cart("sauce-labs-backpack")
    cart_page = products.go_to_cart()
    cart_page.click_checkout()

    # See prior comments.
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_customer_info("Test", "User", "12345")
    overview_page = checkout_page.click_continue()

    # Assert that the product added above is in the cart and finish checkout.
    assert "Sauce Labs Backpack" in overview_page.get_item_list(), "Expected item missing in overview"
    confirmation_page = overview_page.finish_checkout()

    # Retrieves the confirmation header text displayed on the confirmation page.
    # Then, assert that the header is the header indicating a successful checkout.
    header = confirmation_page.get_complete_header()
    assert header == "Thank you for your order!", f"Unexpected confirmation header: {header}"
