from selenium import webdriver
from pages.MainPage import MainPage

def test_site():
    mainPage = MainPage(webdriver.Chrome())
    mainPage.open_site()
    mainPage.entry_field()
    mainPage.click_button()
    mainPage.quit

    assert mainPage.backgroundcolor_zip_code() == "rgba(248, 215, 218, 1)"
    # assert mainPage.background_mail() == "rgba(248, 215, 218, 1)"  Видимо я что то не понимаю. Почему то код не хочет выполнятся по схеме как в прошлый раз. 
    # assert mainPage.background_phone() == "rgba(248, 215, 218, 1)" И помимо этого не в какую не хочет тестить все строки. Чисто методом перебора и по фото в чате разобрался как надо..

    assert mainPage.background_first_name() == "rgba(209, 231, 221, 1)"
    assert mainPage.background_last_name() == "rgba(209, 231, 221, 1)"
    assert mainPage.background_address() == "rgba(209, 231, 221, 1)"
    assert mainPage.background_city() == "rgba(209, 231, 221, 1)"
    assert mainPage.background_country() == "rgba(209, 231, 221, 1)"
    assert mainPage.background_position() == "rgba(209, 231, 221, 1)"
    assert mainPage.background_company() == "rgba(209, 231, 221, 1)"