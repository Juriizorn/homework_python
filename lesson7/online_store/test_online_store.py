from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from StoreMainPage import StoreMainPage
from ProductPage import ProductPage
from CartPage import CartPage
from UserDataPage import UserDataPage
from OrderOverviewPage import OrderOverviewPage

def test_shop():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    main_page = StoreMainPage(driver)
    main_page.open()
    main_page.authorization()
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    cart_page = CartPage(driver)
    cart_page.cart_checkout()
    user_data = UserDataPage(driver)
    user_data.input_user_data()
    overview_page = OrderOverviewPage(driver)
    sum_total = overview_page.get_sum()

    assert sum_total.split("$")[1] == "58.29", f"Вместо ожидаемой итоговой суммы получили {sum_total.split("$")[1]}."
    driver.quit()
