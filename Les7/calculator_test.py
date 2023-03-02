from selenium import webdriver
from pages.CalculatorPage import CalculatorPage

def test_calculator():
    mainPage = CalculatorPage(webdriver.Chrome(), 45)
    mainPage.open_site()
    mainPage.re_timer()
    mainPage.addition()
    mainPage.weit_time()
    assert mainPage.total() == '15'
    
    mainPage.quit