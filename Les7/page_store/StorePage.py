import allure
from selenium.webdriver.common.by import By

class StorePage:
    def __init__(self, browser):
       self.driver = browser
    
    allure.step("Перейти к форме 'Products'")
    def open(self)->None:
        """Функция выполняет открытие страницы"""
        self.driver.get("https://www.saucedemo.com/inventory.html")
    
    allure.step("Добавить в карзину товары")
    def collection(self)->None:
        """Функция выполняет добавление лотов в карзину"""
        self.driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-backpack"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-onesie"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="shopping_cart_container"]').click()