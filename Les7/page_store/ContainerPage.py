import allure
from selenium.webdriver.common.by import By

class CheckPage:
    def __init__(self, browser):
       self.driver = browser
    
    allure.step("Перейти в 'Карзину'")
    def open(self)->None:
        """Функция выполняет открытие страницы"""
        self.driver.get("https://www.saucedemo.com/cart.html")
    
    allure.step("Нажать кнопку 'checkout'")
    def check(self)->None:
        """Функция выполняет открытие страницы авторизации"""
        self.driver.find_element(By.CSS_SELECTOR, '[id="checkout"]').click()