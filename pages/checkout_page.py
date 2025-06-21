# See comment in login_page.py if you need an explanation.
from selenium.webdriver.common.by import By
from pages.overview_page import OverviewPage

# This class represents the Checkout page of the application, following the Page Object Model.
# It will contain locators and methods specific to interacting with the Checkout page.
class CheckoutPage:

    # See comment in login_page.py if you need an explanation.
    def __init__(self, driver):
        self.driver = driver

    # Enters the customer's information (first name, last name, and postal code, which also are the arguments)
    # into the respective input fields on the checkout information page.
    def enter_customer_info(self, first: str, last: str, postal: str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)

    # Clicks the continue button and initializes and returns an instance of the overview page.
    def click_continue(self) -> OverviewPage:
        self.driver.find_element(By.ID, "continue").click()
        return OverviewPage(self.driver)