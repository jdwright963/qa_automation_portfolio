from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def is_logged_in(self) -> bool:
        header = self.driver.find_element(By.CLASS_NAME, "title")
        return header.is_displayed() and header.text == "Products"