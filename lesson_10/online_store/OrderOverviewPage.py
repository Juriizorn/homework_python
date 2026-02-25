import allure
from selenium.webdriver.common.by import By


class OrderOverviewPage:

    def __init__(self, driver) -> None:
        """
        Конструктор класса StoreMainPage.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.browser = driver

    @allure.step("Возвращает полную сумму товаров на странице заказа")
    def get_sum(self) -> str:
        """
        Считывает и возвращает полную сумму товаров на странице заказа.
        """
        sum_total = (self.browser.find_element
                     (By.CSS_SELECTOR, "div.summary_total_label").text)
        return sum_total
