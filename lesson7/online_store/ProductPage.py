from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    def __init__(self, driver):
        self.browser = driver

    def add_to_cart(self):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        waiter = WebDriverWait(self.browser, 15)
        waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link")))
        self.browser.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()