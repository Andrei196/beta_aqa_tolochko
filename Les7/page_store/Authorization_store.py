from selenium.webdriver.common.by import By
class Autorization:
    def __init__(self, browser, name, password):
        self.driver = browser
        self.name = name
        self.password = password

    def open(self):
        self.driver.implicitly_wait(4)
        self.driver.get("https://www.saucedemo.com/")
    
    def autorization(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="user-name"]').send_keys(self.name)
        self.driver.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, '[id="login-button"]').click()