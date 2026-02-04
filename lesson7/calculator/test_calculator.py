from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from MainPageCalc import MainPageCalc

def test_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page_calc = MainPageCalc(driver)
    main_page_calc.open_calc()
    main_page_calc.slow_calc()
    main_page_calc.calculator_data_input()
    main_page_calc.wait_result()
    result = main_page_calc.get_result()

    assert "15" == result, f"Вместо ожидаемого результата получили {result}."

    driver.quit()