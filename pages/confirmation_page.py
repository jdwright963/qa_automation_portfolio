# See comment in login_page.py if you need an explanation.
from selenium.webdriver.common.by import By

# This class represents the Confirmation page of the application, following the Page Object Model.
# It will contain locators and methods specific to interacting with the Confirmation page.
class ConfirmationPage:

    # See comment in login_page.py if you need an explanation.
    def __init__(self, driver):
        self.driver = driver

    # Retrieves the confirmation header text displayed on the confirmation page.
    # It locates the element using the class name "complete-header" and returns the string.
    def get_complete_header(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text