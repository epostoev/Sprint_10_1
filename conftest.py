import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import Addresses
from pages.main_page import MainPage
    
@pytest.fixture
def driver():
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page

@pytest.fixture
def route_set(main_page):
    main_page.set_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
    return main_page