from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.set_window_size(1280, 720)
# Зайти на сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)
# Нажать на close
lokator_modal = "div.modal-footer"
button_click = driver.find_element(By.CSS_SELECTOR, lokator_modal)
button_click.click()
sleep(5)