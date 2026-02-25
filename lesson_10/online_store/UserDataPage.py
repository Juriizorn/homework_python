import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserDataPage:

    def __init__(self, driver) -> None:
        """
        Конструктор класса StoreMainPage.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.browser = driver

    @allure.step("Вводит данные пользователя")
    def input_user_data(self) -> None:
        """
        Вводит в строку "First Name" имя "Юрий".
        Вводит в строку "Last Name" фамилию "Сморчков".
        Вводит в строку "Zip/Postal Code" индекс "397000".
        Выставляет задержку для загрузки элемента страницы в 15 секунд.
        Нажимает на кнопку "continue".
        """
        self.browser.find_element(By.ID, "first-name").send_keys("Юрий")
        self.browser.find_element(By.ID, "last-name").send_keys("Сморчков")
        self.browser.find_element(By.ID, "postal-code").send_keys("397000")
        waiter = WebDriverWait(self.browser, 15)
        waiter.until(EC.element_to_be_clickable((By.ID, "continue")))
        self.browser.find_element(By.ID, "continue").click()
