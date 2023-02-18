from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.set_window_size(1280, 720)
# Зайти на сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
# Пять раз кликнуть на кнопку
lokator_b = "button"
button_klick = driver.find_element(By.CSS_SELECTOR, lokator_b)
for click in range(1,6):
    button_klick.click()
# Собрать со страницы список кнопок Delete
lokator_d ="button.added-manually"
button_klick_d = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(button_klick_d))
sleep(5)