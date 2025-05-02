import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_login_and_add_to_cart(driver):
    # Load and perform login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in(), "Login failed: Products page not displayed"

    # Add product to cart
    products_page = ProductsPage(driver)
    products_page.add_to_cart("sauce-labs-bike-light")
    products_page.go_to_cart()

    # Verify cart contents
    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()
    assert "Sauce Labs Bike Light" in cart_items, f"Expected 'Sauce Labs Bike Light' in cart, got {cart_items}"