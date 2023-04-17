import allure
from selenium import webdriver
from pages.MainPage import MainPage

@allure.epic("Тестовый сайт")
@allure.id("SITE-1")
@allure.story("Проверка валидной работы формы")
@allure.feature("EXPECTATION")
@allure.title("Проверить 'background-color' строк")
@allure.description("Если строка заполнена валидными данными, то цвет фона строки 'зеленый', в ином случае 'красный'")
@allure.severity("NORMAL")
def test_site():
    mainPage = MainPage(webdriver.Chrome())
    mainPage.open()
    mainPage.entry_field()
    mainPage.click_button()
    mainPage.quit
    
    with allure.step("Проверить 'background-color' строки 'Индекс'"):
        assert mainPage.backgroundcolor_zip_code() == "rgba(248, 215, 218, 1)"
    with allure.step("Проверить 'background-color' строки 'Имя'"):
        assert mainPage.background_first_name() == "rgba(209, 231, 221, 1)"
    with allure.step("Проверить 'background-color' строки 'Фамилия'"):
        assert mainPage.background_last_name() == "rgba(209, 231, 221, 1)"
    with allure.step("Проверить 'background-color' строки 'Адрес'"):
        assert mainPage.background_address() == "rgba(209, 231, 221, 1)"
    with allure.step("Проверить 'background-color' строки 'Город'"):
        assert mainPage.background_city() == "rgba(209, 231, 221, 1)"
    with allure.step("Проверить 'background-color' строки 'Страна'"):
        assert mainPage.background_country() == "rgba(209, 231, 221, 1)"
    with allure.step("Проверить 'background-color' строки 'Должность'"):
        assert mainPage.background_position() == "rgba(209, 231, 221, 1)"
    with allure.step("Проверить 'background-color' строки 'Компания'"):
        assert mainPage.background_company() == "rgba(209, 231, 221, 1)"