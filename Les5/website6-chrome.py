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
serch_n_imput = driver.find_element(By.CSS_SELECTOR, lokator_name)
serch_n_imput.send_keys("tomsmith")
sleep(1)
# пороль
lokator_puss = 'input#password'
serch_p_imput = driver.find_element(By.CSS_SELECTOR, lokator_puss)
serch_p_imput.send_keys("SuperSecretPassword!")
sleep(1)
#окес
lokator_log = 'button.radius'
butten_c = driver.find_element(By.CSS_SELECTOR, lokator_log)
butten_c.click()
sleep(2)