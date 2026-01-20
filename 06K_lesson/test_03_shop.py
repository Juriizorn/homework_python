from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    waiter = WebDriverWait(driver, 15)
    waiter.until(EC.element_to_be_clickable((By.ID, "login-button")))
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.shopping_cart_link")))
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Юрий")
    driver.find_element(By.ID, "last-name").send_keys("Сморчков")
    driver.find_element(By.ID, "postal-code").send_keys("39700")
    waiter.until(EC.element_to_be_clickable((By.ID, "continue")))
    driver.find_element(By.ID, "continue").click()
    sum_total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    assert sum_total.split("$")[1] == "58.29", f"Вместо ожидаемой итоговой суммы получили {sum_total.split("$")[1]}."
    driver.quit()