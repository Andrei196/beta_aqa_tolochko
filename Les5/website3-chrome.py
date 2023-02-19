from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1280, 720)
# Зайти на сайт
driver.get("http://uitestingplayground.com/classattr")
# Кликнуть на синюю кнопку
lokator_blue = '[class*="btn-primary"]'
button_click = driver.find_element(By.CSS_SELECTOR, lokator_blue)
# Запустить скрипт 3 раза
x = 0
for click in range(1,4):
    button_click.click()
    x = x+1
assert x == 3
sleep(5)