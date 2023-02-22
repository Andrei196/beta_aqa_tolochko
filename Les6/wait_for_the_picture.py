from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1280, 720)
driver.implicitly_wait(6) #Я выбрал шесть секунд исходя из вкладки нетворк и накинул сверху секунду.
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
img = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
print(img)
sleep(3)