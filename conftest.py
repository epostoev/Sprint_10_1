import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import Addresses
from pages.main_page import MainPage
from pages.order_page import OrderPage

    
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

@pytest.fixture
def fast_route(route_set):
    """Маршрут с выбранным видом 'Быстрый'."""
    route_set.click_mode_fast()
    return route_set

@pytest.fixture
def taxi_order_form(fast_route):
    """Открытая форма заказа такси."""
    fast_route.click_call_taxi()
    return fast_route

@pytest.fixture
def order_page(taxi_order_form):
    return OrderPage(taxi_order_form.driver)
