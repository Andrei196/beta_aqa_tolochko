from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.set_window_size(1280, 720)
# Зайти на сайт
driver.get("http://uitestingplayground.com/dynamicid")
# Кликнуть на синюю кнопку
lokator_b = "[class='btn btn-primary']"
button_klick = driver.find_element(By.CSS_SELECTOR, lokator_b)
# Запустить скрипт 3 раза
x = 0
for click in range(1,4):
    button_klick.click()
    x = x+1
assert x == 3
print(x)
sleep(5)