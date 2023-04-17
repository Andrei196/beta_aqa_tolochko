import allure
from selenium.webdriver.common.by import By

class SwegPage:
    def __init__(self, browser, f_name:str, l_name:str, post_code:int):
       self.driver = browser
       self.fname = f_name
       self.lname = l_name
       self.post = post_code
    
    allure.step("Перейти к форме 'оформление заказа'")
    def open(self):
        """Функция выполняет открытие страницы"""
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
    
    allure.step("Указать в полях данные 'Имя','Фамилия','Индекс получаетля'")
    def Inform(self):
        """Функция выполняет ввод учетных данных"""
        self.driver.find_element(By.CSS_SELECTOR, '[id="first-name"]').send_keys(self.fname)
        self.driver.find_element(By.CSS_SELECTOR, '[id="last-name"]').send_keys(self.lname)
        self.driver.find_element(By.CSS_SELECTOR, '[id="postal-code"]').send_keys(self.post)
    
    allure.step("Нажать кнопку 'continue'")
    def click(self):
        """Функция взаимодействует с кнопкой CONTINUE"""
        self.driver.find_element(By.CSS_SELECTOR, '[id="continue"]').click()