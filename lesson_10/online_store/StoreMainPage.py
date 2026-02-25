import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StoreMainPage:

    def __init__(self, driver) -> None:
        """
        Конструктор класса StoreMainPage.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.browser = driver

    @allure.step("Открытие главной страницы магазина.")
    def open(self) -> None:
        """
        Открывает главную страницу магазина и
        делает максимальный размер экрана.
        """
        self.browser.get("https://www.saucedemo.com/")
        # self.browser.maximize_window()

    @allure.step("Авторизация на главной странице магазина")
    def authorization(self) -> None:
        """
        Авторизует пользователя с именем "standard_user" и
        паролем "secret_sauce".
        Выставляет задержку для загрузки страницы в 15 секунд.
        Нажимает на кнопку "login".
        """
        (self.browser.find_element(By.ID, "user-name")
         .send_keys("standard_user"))
        self.browser.find_element(By.ID, "password").send_keys("secret_sauce")
        waiter = WebDriverWait(self.browser, 15)
        waiter.until(EC.element_to_be_clickable((By.ID, "login-button")))
        self.browser.find_element(By.ID, "login-button").click()
