import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver, timer: int)->int:
        self.driver = driver
        self.timer = timer

    allure.step("Открыть сайт 'Калькулятор'")
    def open(self)->None:
        """Функция выполняет открытие страницы"""
        self.driver.implicitly_wait(4)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    allure.step("В поле таймер установить '45 секунд'")
    def re_timer(self)-> None:
        """Функция обновляет таймер"""
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(self.timer)
    
    allure.step("Ввести данные с клавиатуры 'Калькулятора' 7+8=")
    def addition(self)->None:
        """Функция выполняет ввод данных с калькулятора"""
        self.driver.find_element(By.XPATH,"//span [contains(text(),'7')]").click() 
        self.driver.find_element(By.XPATH,"//span [contains(text(),'+')]").click() 
        self.driver.find_element(By.XPATH,"//span [contains(text(),'8')]").click() 
        self.driver.find_element(By.XPATH,"//span [contains(text(),'=')]").click()
    
    allure.step("Получить результат сложения '15'")
    def wait_time(self)->WebDriverWait: 
       """Ожидание совпадения числа"""
       WebDriverWait(self.driver, self.timer+1).until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR,'.screen') , 'innerHTML', '15'))

    allure.step("Сравнить полученный результат с верным")
    def total(self)->str:
        """Функция принимает данные о сложении"""
        return self.driver.find_element(By.CSS_SELECTOR,'.screen').get_attribute('innerHTML')

    allure.step("Закрыть сайт 'Калькулятор'")      
    def quit(self)->None:
        """Функция выполняет закрытие страницы"""
        self.driver.quit
