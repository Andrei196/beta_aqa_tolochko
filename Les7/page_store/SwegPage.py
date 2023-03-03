from selenium.webdriver.common.by import By

class SwegPage:
    def __init__(self, browser, f_name, l_name, post_code):
       self.driver = browser
       self.fname = f_name
       self.lname = l_name
       self.post = post_code
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
    
    def Inform(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="first-name"]').send_keys(self.fname)
        self.driver.find_element(By.CSS_SELECTOR, '[id="last-name"]').send_keys(self.lname)
        self.driver.find_element(By.CSS_SELECTOR, '[id="postal-code"]').send_keys(self.post)
    
    def click(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="continue"]').click()