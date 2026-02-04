from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageCalc:

    def __init__(self, driver):
        self.browser = driver

    def open_calc(self):
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.browser.maximize_window()

    def slow_calc(self):
        self.browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def calculator_data_input(self):
        self.browser.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text() = '7']").click()
        self.browser.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text() = '+']").click()
        self.browser.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text() = '8']").click()
        self.browser.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text() = '=']").click()

    def wait_result(self):
        waiter = WebDriverWait(self.browser, 50)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    def get_result(self):
        result = self.browser.find_element(By.CSS_SELECTOR, ".screen").text
        return result