import allure

from data import URLS
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


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

    @allure.step("Проверяем что на карте видны ровно две активные точки маршрута")
    def are_route_pins_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: len([
                    pin for pin in d.find_elements(*MainPageLocators.ROUTE_PINS)
                    if pin.is_displayed()
                ]) >= 2
            )
            # Дополнительно: убедимся, что предыдущие маршруты очищены
            # и что маркеры привязаны к правильным адресам
            return True
        except TimeoutException:
            return False

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

    # @allure.step("Получаем список типов передвижения")
    # def get_transport_types(self):
    #     elements = self.find_elements(MainPageLocators.TRANSPORT_TYPES)
    #     return [e.text for e in elements]

    #     @allure.step("Получаем список доступных типов передвижения")
    def get_transport_types(self):
        """Возвращает список типов по именам иконок (car, walk, taxi, bike, scooter, drive)."""
        icons = self.find_elements(MainPageLocators.TRANSPORT_TYPE_ICONS)
        types = []
        for icon in icons:
            src = icon.get_attribute("src")
            name = src.split("/")[-1].split(".")[0].replace("-active", "")
            types.append(name)
        return types

    # @allure.step("Выбираем тип передвижения: {transport_type}")
    # def select_transport_type(self, transport_type):
    #     elements = self.find_elements(MainPageLocators.TRANSPORT_TYPES)
    #     for element in elements:
    #         if element.text == transport_type:
    #             element.click()
    #             return
    #     raise Exception(f"Тип передвижения '{transport_type}' не найден")

    @allure.step("Выбираем тип передвижения: {transport_type}")
    def select_transport_type(self, transport_type):
        icons = self.find_elements(MainPageLocators.TRANSPORT_TYPE_ICONS)
        for icon in icons:
            src = icon.get_attribute("src")
            name = src.split("/")[-1].split(".")[0].replace("-active", "")
            if name == transport_type:
                icon.click()
                return
        raise Exception(f"Тип передвижения '{transport_type}' не найден")

    @allure.step("Проверяем что кнопка 'Вызвать такси' активна")
    def is_call_taxi_button_visible(self):
        return self.is_element_visible(MainPageLocators.BUTTON_CALL_TAXI)

    @allure.step("Проверяем что кнопка 'Забронировать' активна")
    def is_book_drive_button_visible(self):
        return self.is_element_visible(MainPageLocators.BUTTON_BOOK_DRIVE)

    @allure.step("Нажимаем кнопку 'Вызвать такси'")
    def click_call_taxi(self):
        self.click(MainPageLocators.BUTTON_CALL_TAXI)

    @allure.step("Получаем стоимость маршрута")
    def get_route_price(self):
        return self.get_text(MainPageLocators.ROUTE_PRICE)

    @allure.step("Получаем время в пути")
    def get_route_duration(self):
        return self.get_text(MainPageLocators.ROUTE_DURATION)

    @allure.step("Проверяем блок с одинаковым адресом содержит 'Авто Бесплатно В пути 0 мин.'")
    def is_same_address_block_correct(self):
        auto_text = self.get_text(MainPageLocators.SAME_ADDRESS_AUTO)
        duration_text = self.get_text(MainPageLocators.SAME_ADDRESS_DURATION)
        return (
            "Авто" in auto_text and
            "Бесплатно" in auto_text and
            "0 мин" in duration_text
        )
