from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserDataPage:
     def __init__(self, driver):
         self.browser = driver

     def input_user_data(self):
         self.browser.find_element(By.ID, "first-name").send_keys("Юрий")
         self.browser.find_element(By.ID, "last-name").send_keys("Сморчков")
         self.browser.find_element(By.ID, "postal-code").send_keys("39700")
         waiter = WebDriverWait(self.browser, 15)
         waiter.until(EC.element_to_be_clickable((By.ID, "continue")))
         self.browser.find_element(By.ID, "continue").click()