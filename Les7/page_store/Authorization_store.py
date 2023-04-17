import allure
from selenium.webdriver.common.by import By
class Autorization:
    def __init__(self, browser, name:str, password:str):
        self.driver = browser
        self.name = name
        self.password = password

    allure.step("Открыть сайт 'https://www.saucedemo.com/'")
    def open(self)->None:
        """Функция выполняет открытие страницы"""
        self.driver.implicitly_wait(4)
        self.driver.get("https://www.saucedemo.com/")
    
    allure.step("Авторизаваться на сайте")
    def autorization(self)->None:
        """Функция выполняет авторизацию"""
        self.driver.find_element(By.CSS_SELECTOR, '[id="user-name"]').send_keys(self.name)
        self.driver.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, '[id="login-button"]').click()