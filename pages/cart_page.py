from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self) -> list[str]:
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]