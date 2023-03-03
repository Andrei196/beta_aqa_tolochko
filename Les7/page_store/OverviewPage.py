from selenium.webdriver.common.by import By

class Owerview:
    def __init__(self, browser):
       self.driver = browser
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
    
    def total(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.CSS_SELECTOR, '#checkout_summary_container > div > div.summary_info > div.summary_total_label').text
    
    def quit(self):
        self.driver.quit