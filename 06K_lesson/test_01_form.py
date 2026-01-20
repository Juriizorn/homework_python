from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    edge_driver_path = r"C:\Program Files\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
    waiter = WebDriverWait(driver, 15)
    waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    zip_code_field = driver.find_element(By.ID, 'zip-code')
    assert 'alert-danger' in zip_code_field.get_attribute('class'), \
        f"Поле zip-code не заполнено, но не подсвечено красным"

    field_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
    ]
    for field_name in field_to_check:
        field = driver.find_element(By.ID, field_name).get_attribute("class")
        assert "alert-success" in field, f"Поле {field_name} заполнено, но не подсвечено зеленым."
    driver.quit()