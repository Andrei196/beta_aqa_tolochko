from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver, timer):
        self.driver = driver
        self.timer = timer

    def open_site(self):
        self.driver.implicitly_wait(4)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def re_timer(self):
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(self.timer)
    
    def addition(self):
        self.driver.find_element(By.XPATH,"//span [contains(text(),'7')]").click() 
        self.driver.find_element(By.XPATH,"//span [contains(text(),'+')]").click() 
        self.driver.find_element(By.XPATH,"//span [contains(text(),'8')]").click() 
        self.driver.find_element(By.XPATH,"//span [contains(text(),'=')]").click()
    
    def wait_time(self): 
       WebDriverWait(self.driver, self.timer+1).until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR,'.screen') , 'innerHTML', '15'))

    def total(self):
        return self.driver.find_element(By.CSS_SELECTOR,'.screen').get_attribute('innerHTML')
          
    def quit(self):
        self.driver.quit
