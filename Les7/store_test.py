from time import sleep
from selenium import webdriver
from page_store.Authorization_store import Autorization
from page_store.StorePage import StorePage
from page_store.ContainerPage import CheckPage
from page_store.SwegPage import SwegPage
from page_store.OverviewPage import Owerview

def test_online_store():
    browser = webdriver.Chrome()
    
    autoPage = Autorization(browser, "standard_user", "secret_sauce")
    autoPage.open()
    autoPage.autorization()
    
    storPage = StorePage(browser)
    storPage.open()
    storPage.collection()

    checkPage = CheckPage(browser)
    checkPage.open()
    checkPage.check()

    swegPage = SwegPage(browser, "Пюрешка", "Скотлетками", "111222")
    swegPage.open()
    swegPage.Inform()
    swegPage.click()

    total_Ower = Owerview(browser)
    total_Ower.open()
    total_Ower.quit()
    assert total_Ower.total() == "Total: $58.29"   