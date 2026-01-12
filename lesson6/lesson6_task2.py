from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput?")
new_button_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
new_button_name.send_keys("SkyPro")
updating_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
updating_button.click()
print(updating_button.text)
driver.quit()