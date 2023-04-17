import allure
from selenium import webdriver
from calculator.CalculatorPage import CalculatorPage

@allure.epic("Калькулятор")
@allure.id("CALCULATOR-1")
@allure.story("Сравнение ФР с ОР")
@allure.feature("EXPECTATION")
@allure.title("Проверка коректной работы таймера")
@allure.description("Таймер ожидает '45 секунд', чтобы получить результат вычислений")
@allure.severity("CRITICAL")
def test_calculator():
    mainPage = CalculatorPage(webdriver.Chrome(), 45)
    mainPage.open()
    mainPage.re_timer()
    mainPage.addition()
    mainPage.wait_time()
    mainPage.quit()
    
    with allure.step("Сравнение ФР с ОР"):
        assert mainPage.total() == '15'