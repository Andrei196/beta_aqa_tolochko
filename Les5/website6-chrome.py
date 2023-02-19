from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.set_window_size(1280, 720)
# Зайти на сайт
driver.get("http://the-internet.herokuapp.com/login")
# логин
lokator_name = 'input#username'
search_name_imput = driver.find_element(By.CSS_SELECTOR, lokator_name)
search_name_imput.send_keys("tomsmith")
sleep(1)
# пороль
lokator_puss = 'input#password'
search_puss_imput = driver.find_element(By.CSS_SELECTOR, lokator_puss)
search_puss_imput.send_keys("SuperSecretPassword!")
sleep(1)
#окес
lokator_log = 'button.radius'
button_click = driver.find_element(By.CSS_SELECTOR, lokator_log)
button_click.click()
sleep(2)