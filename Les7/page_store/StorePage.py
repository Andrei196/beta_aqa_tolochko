from selenium.webdriver.common.by import By

class StorePage:
    def __init__(self, browser):
       self.driver = browser
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
    
    def collection(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-backpack"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-onesie"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="shopping_cart_container"]').click()