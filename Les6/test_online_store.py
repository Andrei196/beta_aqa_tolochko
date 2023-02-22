from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_store():
    driver = webdriver.Chrome()
    driver.set_window_size(1280, 720)
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.CSS_SELECTOR, '[id="user-name"]').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '[id="login-button"]').click()
    driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    driver.find_element(By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-onesie"]').click()
    driver.find_element(By.CSS_SELECTOR, '[id="shopping_cart_container"]').click()
    driver.find_element(By.CSS_SELECTOR, '[id="checkout"]').click()
    
    driver.find_element(By.CSS_SELECTOR, '[id="first-name"]').send_keys("Пюрешка")
    driver.find_element(By.CSS_SELECTOR, '[id="last-name"]').send_keys("Скотлетками")
    driver.find_element(By.CSS_SELECTOR, '[id="postal-code"]').send_keys("111222")
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '[id="continue"]').click()
    driver.implicitly_wait(5)
    total = driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]')
    txt = total.text
    print(txt)
    driver.quit