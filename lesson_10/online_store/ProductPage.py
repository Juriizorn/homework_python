import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver) -> None:
        """
        Конструктор класса StoreMainPage.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.browser = driver

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self) -> None:
        """
        Добавляет товары (sauce-labs-backpack,
        sauce-labs-bolt-t-shirt, sauce-labs-onesie) в корзину.
        Выставляет задержку для загрузки элемента страницы в 15 секунд.
        Нажимает на кнопку с изображением корзины.
        """
        (self.browser.find_element
         (By.ID, "add-to-cart-sauce-labs-backpack")
         .click())
        (self.browser.find_element
         (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click())
        (self.browser.find_element
         (By.ID, "add-to-cart-sauce-labs-onesie").click())
        waiter = WebDriverWait(self.browser, 15)
        waiter.until(EC.element_to_be_clickable
                     ((By.CSS_SELECTOR, "a.shopping_cart_link")))
        (self.browser.find_element
         (By.CSS_SELECTOR, "a.shopping_cart_link").click())
