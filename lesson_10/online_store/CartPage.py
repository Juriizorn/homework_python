import allure
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver) -> None:
        """
        Конструктор класса StoreMainPage.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.browser = driver

    @allure.step("Нажимает в корзине на кнопку checkout")
    def cart_checkout(self) -> None:
        """
        Нажимает на кнопку "checkout".
        """
        self.browser.find_element(By.ID, "checkout").click()
