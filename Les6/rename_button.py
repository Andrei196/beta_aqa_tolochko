from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1280, 720)

driver.get("http://uitestingplayground.com/textinput")
search_imput = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_imput.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
driver.implicitly_wait(4)
content_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(content_button)
sleep(1)