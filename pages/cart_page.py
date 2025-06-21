# See comment in login_page.py if you need an explanation.
from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage

# This class represents the Cart page of the application, following the Page Object Model.
# It will contain locators and methods specific to interacting with the Cart page.
class CartPage:

    # See comment in login_page.py if you need an explanation.
    def __init__(self, driver):
        self.driver = driver

    # Retrieves a list of all item names displayed on the cart page.
    def get_cart_items(self) -> list[str]:

        # Find all web elements that represent item names on the page.
        # These are identified by the class name "inventory_item_name".
        # 'find_elements' (plural) returns a list of WebElement objects.
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        # Use a list comprehension to iterate through the items.
        # For each item, extract its visible text content.
        # This creates a new list containing only the item names.
        return [item.text for item in items]

    # Retrieves a list of prices for all items currently displayed in the cart.
    # removes the "$" currency symbol, and converts the remaining string to a float.
    def get_item_prices(self) -> list[float]:

        # Find all web elements on the page that display the prices of items in the cart.
        # These are identified by the class name "inventory_item_price".
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        # Use a list comprehension to iterate through the prices and for each element:
        # Get the text of the price element, remove the dollar sign character from the text
        # Convert the string into a float. The result is a new list containing these prices.t
        return [float(price.text.replace("$", "")) for price in prices]

    # Clicks the checkout button.
    def click_checkout(self) -> CheckoutPage:

        # Self explanatory based on prior comments.
        self.driver.find_element(By.ID, "checkout").click()
        return CheckoutPage(self.driver)