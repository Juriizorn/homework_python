from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, 'button').click()

secure_area = driver.find_element(By.CSS_SELECTOR, '#flash').text
print(secure_area)

driver.quit()
