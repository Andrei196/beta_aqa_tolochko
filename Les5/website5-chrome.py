from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.set_window_size(1280, 720)
# Зайти на сайт
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)
# Нажать на close
lokator_num = '[type="number"]'
serch_imput = driver.find_element(By.CSS_SELECTOR, lokator_num)
serch_imput.send_keys("1000", Keys.RETURN)
sleep(2)
serch_imput.clear()
sleep(1)
serch_imput.send_keys("SkyPro", Keys.RETURN) #не работать :3
sleep(2)
serch_imput.send_keys("4", Keys.RETURN)

sleep(2)