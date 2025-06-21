# See comment in login_page.py if you need an explanation.
from selenium.webdriver.common.by import By
from pages.confirmation_page import ConfirmationPage

# This class represents the Overview page (this is a page to review your order before submitting) of the application,
# following the Page Object Model. It will contain locators and methods specific to interacting with the Overview page.
class OverviewPage:

    # See comment in login_page.py if you need an explanation.
    def __init__(self, driver):
        self.driver = driver

    # Clicks the finish button, and initializes and returns the confirmation page object.
    def finish_checkout(self) -> ConfirmationPage:
        self.driver.find_element(By.ID, "finish").click()
        return ConfirmationPage(self.driver)

    # Retrieves a list of all item names displayed on the checkout overview page.
    def get_item_list(self) -> list[str]:

        # Find all web elements that represent item names on the page.
        # These are identified by the class name "inventory_item_name".
        # 'find_elements' (plural) returns a list of WebElement objects.
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        # Use a list comprehension to iterate through the items.
        # For each item, extract its visible text content.
        # This creates a new list containing only the item names.
        return [item.text for item in items]
    
    # Retrieves the "Item total" amount (subtotal before tax).
    def get_item_total(self) -> float:

        # Find the element displaying the item total using its class name.
        # The text is expected to be in the format "Item total: $XX.YY"
        item_total_element = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        item_total_text = item_total_element.text

        # Extract the numerical value by splitting the string at "$" and taking the second part.
        # Strip any leading/trailing whitespace just in case.
        price_str = item_total_text.split("$")[1].strip()
        return float(price_str)
