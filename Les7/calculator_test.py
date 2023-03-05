from selenium import webdriver
from pages.CalculatorPage import CalculatorPage

def test_calculator():
    mainPage = CalculatorPage(webdriver.Chrome(), 45)
    mainPage.open()
    mainPage.re_timer()
    mainPage.addition()
    mainPage.wait_time()
    assert mainPage.total() == '15'
    
    mainPage.quit