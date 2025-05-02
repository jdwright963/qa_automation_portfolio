from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id: str) -> None:
        # product_id should match the suffix of the button ID, e.g., "sauce-labs-bike-light"
        button_id = f"add-to-cart-{product_id}"
        self.driver.find_element(By.ID, button_id).click()

    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()