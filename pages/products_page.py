# See comment in login_page.py if you need an explanation.
from selenium.webdriver.common.by import By
from pages.cart_page import CartPage

# This class represents the Products page of the application, following the Page Object Model.
# It will contain locators and methods specific to interacting with the Products page.
class ProductsPage:

    # See comment in login_page.py if you need an explanation.
    def __init__(self, driver):
        self.driver = driver

    # Adds a specific product (based on the product_id provided) to the shopping cart by clicking its "Add to cart" button.
    def add_to_cart(self, product_id: str) -> None:
        button_id = f"add-to-cart-{product_id}"
        self.driver.find_element(By.ID, button_id).click()

    # Removes a specific product (based on the product_id provided) from the shopping cart by clicking its "Remove" button.
    # There is actually a Remove button in both the products page and the cart page. 
    def remove_from_cart(self, product_id: str) -> None:
        button_id = f"remove-{product_id}"
        self.driver.find_element(By.ID, button_id).click()

    # Navigates to the shopping cart page by clicking the shopping cart icon, 
    # and initialize and return an instance of the CartPage.
    def go_to_cart(self) -> CartPage:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return CartPage(self.driver)

    # Retrieves the current count displayed on the shopping cart badge (the number of items in the cart).
    def get_cart_badge_count(self) -> int:

        # Find the shopping cart badge element by its class name.
        # Then, get the text content of this element.
        badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

        # Return the text as an int.
        return int(badge)