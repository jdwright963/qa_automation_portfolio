# Import the 'By' class from Selenium's common utilities.
# The 'By' class is used to specify the strategy for locating elements on a web page
# (e.g. by ID, by NAME, by XPATH, by CSS_SELECTOR).
from selenium.webdriver.common.by import By

# This class represents the login page of the application, following the Page Object Model.
# It will contain locators and methods specific to interacting with the login page.
class LoginPage:
    URL = "https://www.saucedemo.com/"

    # Constructor for the class.
    # This method is automatically called when a new LoginPage object is created.
    # The driver that is passed to it is the Selenium WebDriver instance that 
    # will be used to interact with the browser and the elements on the login page.
    def __init__(self, driver):

        # Store the provided WebDriver instance as an instance variable 'self.driver'.
        # This makes the driver accessible to all other methods within this LoginPage object.
        self.driver = driver

        # Navigate the browser to the login page's URL.
        self.driver.get(self.URL)

    # Enters credentials and clicks the login button.
    # Args are the username to be entered into the username field, and the password to be entered 
    # into the password field.
    def login(self, username: str, password: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    # Checks if the user is successfully logged in by verifying the presence and
    # text of the "Products" page header after a login attempt.
    # Returns True if the header is displayed and its text is "Products", False otherwise.
    def is_logged_in(self) -> bool:
        header = self.driver.find_element(By.CLASS_NAME, "title")
        return header.is_displayed() and header.text == "Products"

    # Checks if an error message is displayed on the page, typically after a failed
    # login attempt. It locates the error message element using a CSS selector "h3[data-test='error']".
    # Returns True if the error message element is found and visible, False otherwise.
    def error_message_displayed(self) -> bool:
        error = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        return error.is_displayed()