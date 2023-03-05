from selenium.webdriver.common.by import By
class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.implicitly_wait(4)
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    
    def entry_field(self):
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
    
    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="btn btn-outline-primary mt-3"]').click()
    
    def background_first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#first-name').value_of_css_property("background-color")
    def background_last_name(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#last-name').value_of_css_property("background-color")
    def background_address(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#address').value_of_css_property("background-color")
    def backgroundcolor_zip_code(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#zip-code').value_of_css_property("background-color")  
    def background_mail(self):
        assert self.driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property("background-color")
    def background_phone(self):
        assert self.driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property("background-color")
    def background_city(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#city').value_of_css_property("background-color")
    def background_country(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#country').value_of_css_property("background-color")
    def background_position(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#job-position').value_of_css_property("background-color")
    def background_company(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#company').value_of_css_property("background-color")

    def quit(self):
        self.driver.quit