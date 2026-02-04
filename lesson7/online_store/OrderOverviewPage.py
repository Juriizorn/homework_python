from selenium.webdriver.common.by import By

class OrderOverviewPage:

    def __init__(self, driver):
        self.browser = driver

    def get_sum(self):
        sum_total = self.browser.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return sum_total