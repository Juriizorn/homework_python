import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager

from StoreMainPage import StoreMainPage
from ProductPage import ProductPage
from CartPage import CartPage
from UserDataPage import UserDataPage
from OrderOverviewPage import OrderOverviewPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager()
                                                      .install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование суммы товаров в заказе онлайн магазина")
@allure.description("Тест проверяет итоговую сумму выбранных "
                    "вещей при оформлении заказа")
@allure.feature("Онлайн магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver: WebDriver):
    """
    Тест проверяет итоговую сумму выбранных вещей при оформлении заказа.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.

    """
    main_page = StoreMainPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    user_data = UserDataPage(driver)
    overview_page = OrderOverviewPage(driver)

    with allure.step("Открытие главной страницы магазина"):
        main_page.open()
    with allure.step("Авторизация на главной странице магазина"):
        main_page.authorization()
    with allure.step("Добавляет товары в корзину"):
        product_page.add_to_cart()
    with allure.step("Нажимает в корзине на кнопку checkout"):
        cart_page.cart_checkout()
    with allure.step("Вводит данные пользователя"):
        user_data.input_user_data()
    with allure.step("Возвращает полную сумму товаров на странице заказа"):
        sum_total = overview_page.get_sum()
    with (allure.step("Проверка результата")):
        assert sum_total.split("$")[1] == "58.29", \
            (f"Вместо ожидаемой итоговой суммы получили "
             f"{sum_total.split("$")[1]}.")
