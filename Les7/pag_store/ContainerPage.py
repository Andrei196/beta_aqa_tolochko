from selenium.webdriver.common.by import By

class CheckPage:
    def __init__(self, browser):
       self.driver = browser
    
    def get(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
    
    def check(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="checkout"]').click()