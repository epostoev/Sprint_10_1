import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def _find_tariff_card(self, tariff_name):
        """Находит карточку тарифа по названию."""
        cards = self.find_elements(OrderPageLocators.TARIFF_CARD)
        for card in cards:
            title = self.find_child_element(card, OrderPageLocators.TARIFF_CARD_TITLE)
            text = self.get_inner_text(title).strip()
            if text == tariff_name:
                return card
        raise Exception(f"Тариф '{tariff_name}' не найден")

    @allure.step("Получаем список тарифов")
    def get_tariff_names(self):
        cards = self.find_elements(OrderPageLocators.TARIFF_CARD)
        names = []
        for card in cards:
            title = self.find_child_element(card, OrderPageLocators.TARIFF_CARD_TITLE)
            names.append(self.get_inner_text(title).strip())
        return names

    @allure.step("Проверяем что отображается один активный тариф")
    def is_one_tariff_active(self):
        active = self.find_elements(OrderPageLocators.TARIFF_CARD_ACTIVE)
        return len(active) == 1

    @allure.step("Наводим курсор на кнопку i тарифа '{tariff_name}' и получаем описание")
    def get_tariff_description_on_hover(self, tariff_name):
        """Наводит курсор на кнопку i тарифа и возвращает текст описания из попапа."""
        self.select_tariff(tariff_name)

        def hover_and_get_text(driver):
            # Заново ищем карточку — React перерисовывает DOM после клика
            card = self._find_tariff_card(tariff_name)
            i_button = self.find_child_element(card, OrderPageLocators.TARIFF_I_BUTTON)
            self.scroll_to_element(i_button)
            self.hover_element(i_button)
            element = self.find_child_element(card, OrderPageLocators.TARIFF_POPUP_DESCRIPTION)
            text = self.get_inner_text(element).strip()
            return text if text else False

        return self.wait_until(hover_and_get_text, timeout=15)

    @allure.step("Проверяем что блок полей заказа отображается")
    def is_order_fields_visible(self):
        return (
            self.is_element_visible(OrderPageLocators.FIELD_PHONE) and
            self.is_element_visible(OrderPageLocators.FIELD_PAYMENT) and
            self.is_element_visible(OrderPageLocators.FIELD_COMMENT) and
            self.is_element_visible(OrderPageLocators.FIELD_REQUIREMENTS)
        )

    @allure.step("Выбираем тариф: {tariff_name}")
    def select_tariff(self, tariff_name):
        card = self._find_tariff_card(tariff_name)
        card.click()

    @allure.step("Включаем чекбокс 'Столик для ноутбука'")
    def enable_laptop_table(self):
        # Слайдер перекрывает скрытый input, поэтому кликаем через JS
        checkbox = self.find_element(OrderPageLocators.CHECKBOX_LAPTOP_TABLE)
        self.scroll_to_element(checkbox)
        self.click_js(OrderPageLocators.CHECKBOX_LAPTOP_TABLE)

    @allure.step("Проверяем что чекбокс 'Столик для ноутбука' включён")
    def is_laptop_table_enabled(self):
        checkbox = self.find_element(OrderPageLocators.CHECKBOX_LAPTOP_TABLE_INPUT)
        return checkbox.is_selected()

    @allure.step("Нажимаем кнопку 'Ввести номер и заказать'")
    def click_order_button(self):
        self.click(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Проверяем что отображается окно поиска машины")
    def is_search_window_visible(self):
        if not self.is_element_visible(OrderPageLocators.ORDER_HEADER_TITLE):
            return False
        return self.get_text(OrderPageLocators.ORDER_HEADER_TITLE) == "Поиск машины"

    @allure.step("Проверяем что таймер обратного отсчёта отображается")
    def is_timer_visible(self):
        return self.is_element_visible(OrderPageLocators.ORDER_TIMER)

    @allure.step("Проверяем что кнопки 'Отменить' и 'Детали' отображаются")
    def are_order_buttons_visible(self):
        return (
            self.is_element_visible(OrderPageLocators.BUTTON_CANCEL) and
            self.is_element_visible(OrderPageLocators.BUTTON_DETAILS)
        )

    @allure.step("Ждём окно совершённого заказа (заголовок 'приедет')")
    def wait_for_order_completed(self, timeout=60):
        self.wait_for_text_in_element(
            OrderPageLocators.ORDER_HEADER_TITLE, "приедет", timeout=timeout)

    @allure.step("Получаем заголовок окна заказа")
    def get_order_header_text(self):
        return self.get_text(OrderPageLocators.ORDER_HEADER_TITLE)

    @allure.step("Проверяем что окно совершённого заказа отображается")
    def is_completed_order_window_visible(self):
        return (
            self.is_element_visible(OrderPageLocators.ORDER_NUMBER) and
            self.is_element_visible(OrderPageLocators.ORDER_DRIVER_RATING) and
            self.are_order_buttons_visible()
        )

    @allure.step("Нажимаем кнопку 'Детали'")
    def click_details(self):
        self.click(OrderPageLocators.BUTTON_DETAILS)

    @allure.step("Нажимаем кнопку 'Отмена'")
    def click_cancel(self):
        self.click(OrderPageLocators.BUTTON_CANCEL)

    @allure.step("Получаем стоимость из деталей заказа")
    def get_details_price_text(self):
        return self.get_text(OrderPageLocators.ORDER_DETAILS_PRICE)

    @allure.step("Проверяем что детали заказа видны")
    def is_order_details_visible(self):
        return self.is_element_visible(OrderPageLocators.ORDER_DETAILS)

    @allure.step("Проверяем что окно заказа закрылось")
    def is_order_window_closed(self):
        return self.wait_for_element_invisible(OrderPageLocators.ORDER_WINDOW, timeout=5)