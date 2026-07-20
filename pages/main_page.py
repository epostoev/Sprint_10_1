import allure

from data import URLS
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем главную страницу")
    def open(self):
        self.go_to_url(URLS.BASE_URL)

    @allure.step("Вводим адрес 'Откуда': {address}")
    def enter_from_address(self, address):
        self.enter_text(MainPageLocators.INPUT_FROM, address)

    @allure.step("Вводим адрес 'Куда': {address}")
    def enter_to_address(self, address):
        self.enter_text(MainPageLocators.INPUT_TO, address)

    @allure.step("Вводим маршрут")
    def set_route(self, from_address, to_address):
        self.enter_from_address(from_address)
        self.enter_to_address(to_address)

    @allure.step("Проверяем что на карте отображаются две точки маршрута")
    def are_route_pins_visible(self):
        pins = self.find_elements(MainPageLocators.ROUTE_PINS)
        return len(pins) >= 2

    @allure.step("Проверяем что блок выбора маршрута отображается")
    def is_modes_container_visible(self):
        return self.is_element_visible(MainPageLocators.MODES_CONTAINER)

    @allure.step("Получаем текст активного таба маршрута")
    def get_active_mode(self):
        return self.get_text(MainPageLocators.MODE_ACTIVE)

    @allure.step("Кликаем на таб 'Оптимальный'")
    def click_mode_optimal(self):
        self.click(MainPageLocators.MODE_OPTIMAL)

    @allure.step("Кликаем на таб 'Быстрый'")
    def click_mode_fast(self):
        self.click(MainPageLocators.MODE_FAST)

    @allure.step("Кликаем на таб 'Свой'")
    def click_mode_custom(self):
        self.click(MainPageLocators.MODE_CUSTOM)

    @allure.step("Получаем список типов передвижения")
    def get_transport_types(self):
        elements = self.find_elements(MainPageLocators.TRANSPORT_TYPES)
        return [e.text for e in elements]

    @allure.step("Проверяем что кнопка 'Вызвать такси' активна")
    def is_call_taxi_button_visible(self):
        return self.is_element_visible(MainPageLocators.BUTTON_CALL_TAXI)

    @allure.step("Проверяем что кнопка 'Забронировать' активна")
    def is_book_drive_button_visible(self):
        return self.is_element_visible(MainPageLocators.BUTTON_BOOK_DRIVE)

    @allure.step("Нажимаем кнопку 'Вызвать такси'")
    def click_call_taxi(self):
        self.click(MainPageLocators.BUTTON_CALL_TAXI)

    @allure.step("Проверяем блок с одинаковым адресом содержит 'Авто Бесплатно В пути 0 мин.'")
    def is_same_address_block_correct(self):
        auto_text = self.get_text(MainPageLocators.SAME_ADDRESS_AUTO)
        duration_text = self.get_text(MainPageLocators.SAME_ADDRESS_DURATION)
        return (
            "Авто" in auto_text and
            "Бесплатно" in auto_text and
            "0 мин" in duration_text
        )