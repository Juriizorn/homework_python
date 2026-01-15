from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput?")
new_button_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
new_button_name.send_keys("SkyPro")
updating_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
updating_button.click()
waiter = WebDriverWait(driver, 20)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))
print(updating_button.text)
driver.quit()