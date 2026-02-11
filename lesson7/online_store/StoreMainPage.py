from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StoreMainPage:

     def __init__(self, driver):
         self.browser = driver

     def open(self):
         self.browser.get("https://www.saucedemo.com/")
         self.browser.maximize_window()

     def authorization(self):
         self.browser.find_element(By.ID, "user-name").send_keys("standard_user")
         self.browser.find_element(By.ID, "password").send_keys("secret_sauce")
         waiter = WebDriverWait(self.browser, 15)
         waiter.until(EC.element_to_be_clickable((By.ID, "login-button")))
         self.browser.find_element(By.ID, "login-button").click()

