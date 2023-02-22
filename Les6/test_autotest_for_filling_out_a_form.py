from selenium import webdriver
from selenium.webdriver.common.by import By

def test_backgroundcolor():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(10)

    driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
    
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-outline-primary mt-3"]').click()

    assert driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)" # только одно я не понял.... Почему то локатор не захотел передаваться как в первой группе. Пришлось сокращать до решетки.
    assert driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color") == "rgba(248, 215, 218, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color") == "rgba(248, 215, 218, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color") == "rgba(248, 215, 218, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

    driver.quit
