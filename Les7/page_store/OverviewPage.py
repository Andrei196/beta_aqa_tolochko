import allure
from selenium.webdriver.common.by import By

class Owerview:
    def __init__(self, browser):
       self.driver = browser
    
    allure.step("Перейти к форме 'оформление заказа'")
    def open(self)->None:
        """Функция выполняет открытие страницы"""
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
    
    allure.step("Получить финальную стоимость заказа")
    def total(self)->str:
        """Функция получает данные цены"""
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.CSS_SELECTOR, '#checkout_summary_container > div > div.summary_info > div.summary_total_label').text
    
    allure.step("Закрыть форму")
    def quit(self)->None:
        """Функция выполняет закрытие страницы"""
        self.driver.quit