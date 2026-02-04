from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.browser = driver

    def cart_checkout(self):
        self.browser.find_element(By.ID, "checkout").click()