import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
class MainPage:
    def __init__(self, driver):
        self.driver = driver

    allure.step("Открыть сайт 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'")
    def open(self)->None:
        """Функция выполняет открытие страницы"""
        self.driver.implicitly_wait(4)
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    
    allure.step("Заполнить строки: Имя, Фамилия, Адрес, Город, Страна, Должнось, Компания.")
    def entry_field(self)->None:
        """Функция выполняет ввод данных"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
        self.driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
    
    allure.step("Нажать кнопку 'SUBMIT'")
    def click_button(self)->None:
        """Функция выполняет нажатие на кнопку SUBMIT"""
        self.driver.find_element(By.CSS_SELECTOR, '[class="btn btn-outline-primary mt-3"]').click()
    
    allure.step("Проверить цвет заднего фона 'Имя'")
    def background_first_name(self)->str:
        """Функция выполняет проверку цвета заднего фона ИМЯ"""
        return self.driver.find_element(By.CSS_SELECTOR,'#first-name').value_of_css_property("background-color")
    
    allure.step("Проверить цвет заднего фона 'Фамилия'")
    def background_last_name(self)->str:
        """Функция выполняет проверку цвета заднего фона ФАМИЛИЯ"""
        return self.driver.find_element(By.CSS_SELECTOR,'#last-name').value_of_css_property("background-color")
    
    allure.step("Проверить цвет заднего фона 'Адрес'")
    def background_address(self)->str:
        """Функция выполняет проверку цвета заднего фона АДРЕС"""
        return self.driver.find_element(By.CSS_SELECTOR,'#address').value_of_css_property("background-color")
    
    allure.step("Проверить цвет заднего фона 'Индекс'")
    def backgroundcolor_zip_code(self)->str:
        """Функция выполняет проверку цвета заднего фона ИНДЕКС"""
        return self.driver.find_element(By.CSS_SELECTOR,'#zip-code').value_of_css_property("background-color")  
    
    allure.step("Проверить цвет заднего фона 'Город'")
    def background_city(self)->str:
        """Функция выполняет проверку цвета заднего фона ГОРОД"""
        return self.driver.find_element(By.CSS_SELECTOR,'#city').value_of_css_property("background-color")
    
    allure.step("Проверить цвет заднего фона 'Страна'")
    def background_country(self)->str:
        """Функция выполняет проверку цвета заднего фона СТРАНА"""
        return self.driver.find_element(By.CSS_SELECTOR,'#country').value_of_css_property("background-color")
    
    allure.step("Проверить цвет заднего фона 'Должность'")
    def background_position(self)->str:
        """Функция выполняет проверку цвета заднего фона ДОЛЖНОМТЬ"""
        return self.driver.find_element(By.CSS_SELECTOR,'#job-position').value_of_css_property("background-color")
    
    allure.step("Проверить цвет заднего фона 'Компания'")
    def background_company(self)->str:
        """Функция выполняет проверку цвета заднего фона НАЗВАНИЕ КОМПАНИИ"""
        return self.driver.find_element(By.CSS_SELECTOR,'#company').value_of_css_property("background-color")

    allure.step("Закрыть страницу")
    def quit(self)->None:
        """Функция выполняет закрытие страницы"""
        self.driver.quit