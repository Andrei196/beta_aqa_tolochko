from time import sleep
from selenium import webdriver
from pag_store.Authorization_store import Autorization
from pag_store.StorePage import StorePage
from pag_store.ContainerPage import CheckPage
from pag_store.SwegPage import SwegPage
from pag_store.OverviewPage import Owerview

def test_online_store():
    browser = webdriver.Chrome()
    
    autoPage = Autorization(browser, "standard_user", "secret_sauce")
    autoPage.open_site()
    autoPage.autorization()
    
    storPage = StorePage(browser)
    storPage.get()
    storPage.collection()

    checkPage = CheckPage(browser)
    checkPage.get()
    checkPage.check()

    swegPage = SwegPage(browser, "Пюрешка", "Скотлетками", "111222")
    swegPage.get()
    swegPage.Inform()
    swegPage.click()

    total_O = Owerview(browser)
    total_O.get()
    total_O.quit()
    assert total_O.total() == "Total: $58.29"   