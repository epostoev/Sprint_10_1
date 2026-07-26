import allure

from data import TariffNames, TariffDescriptions
from pages.order_page import OrderPage


@allure.feature("Заказ тарифа Такси")
class TestTaxiOrder:

    @allure.title("Форма заказа содержит все 6 тарифов, один из них активный")
    def test_order_form_has_six_tariffs_one_active(self, taxi_order_form):
        order_page = OrderPage(taxi_order_form.driver)
        tariff_names = order_page.get_tariff_names()
        missing = [n for n in TariffNames.ALL if n not in tariff_names]
        assert (
            len(tariff_names) == 6
            and not missing
            and order_page.is_one_tariff_active()
        ), f"Тарифы некорректны: найдено {tariff_names}, отсутствуют {missing}"

    @allure.title("Описание тарифа 'Рабочий' соответствует ТЗ")
    def test_worker_tariff_description(self, taxi_order_form):
        order_page = OrderPage(taxi_order_form.driver)
        description = order_page.get_tariff_description_on_hover(
            TariffNames.WORKER)
        assert description == TariffDescriptions.WORKER, \
            f"Описание не соответствует ТЗ: '{description}'"

    @allure.title("Описание тарифа 'Отпускной' соответствует ТЗ")
    def test_vacation_tariff_description(self, taxi_order_form):
        order_page = OrderPage(taxi_order_form.driver)
        description = order_page.get_tariff_description_on_hover(
            TariffNames.VACATION)
        assert description == TariffDescriptions.VACATION, \
            f"Описание не соответствует ТЗ: '{description}'"

    @allure.title("Описание тарифа 'Утешительный' соответствует ТЗ")
    def test_comfort_tariff_description(self, taxi_order_form):
        order_page = OrderPage(taxi_order_form.driver)
        description = order_page.get_tariff_description_on_hover(
            TariffNames.COMFORT)
        assert description == TariffDescriptions.COMFORT, \
            f"Описание не соответствует ТЗ: '{description}'"

    @allure.title("Описание тарифа 'Глянцевый' соответствует ТЗ")
    def test_glossy_tariff_description(self, taxi_order_form):
        order_page = OrderPage(taxi_order_form.driver)
        description = order_page.get_tariff_description_on_hover(
            TariffNames.GLOSSY)
        assert description == TariffDescriptions.GLOSSY, \
            f"Описание не соответствует ТЗ: '{description}'"

    @allure.title("Описание тарифа 'Сонный' соответствует ТЗ")
    def test_sleepy_tariff_description(self, taxi_order_form):
        order_page = OrderPage(taxi_order_form.driver)
        description = order_page.get_tariff_description_on_hover(
            TariffNames.SLEEPY)
        assert description == TariffDescriptions.SLEEPY, \
            f"Описание не соответствует ТЗ: '{description}'"

    @allure.title("Описание тарифа 'Разговорчивый' соответствует ТЗ")
    def test_talkative_tariff_description(self, taxi_order_form):
        order_page = OrderPage(taxi_order_form.driver)
        description = order_page.get_tariff_description_on_hover(
            TariffNames.TALKATIVE)
        assert description == TariffDescriptions.TALKATIVE, \
            f"Описание не соответствует ТЗ: '{description}'"

    @allure.title("Под тарифами отображаются поля Телефон, Способ оплаты, Комментарий")
    def test_order_fields_visible_below_tariffs(self, taxi_order_form):
        order_page = OrderPage(taxi_order_form.driver)
        assert order_page.is_order_fields_visible(), \
            "Поля заказа не отображаются"


@allure.feature("Заказ тарифа Такси — полный флоу")
class TestTaxiOrderFlow:

    @allure.title("После заказа отображается окно ожидания машины со всеми элементами по ТЗ")
    def test_search_window_has_all_elements(self, order_page):
        order_page.select_tariff(TariffNames.WORKER)
        order_page.enable_laptop_table()
        order_page.click_order_button()
        assert (
            order_page.is_search_window_visible()
            and order_page.is_timer_visible()
            and order_page.are_order_buttons_visible()
        ), "Окно ожидания машины не содержит все элементы по ТЗ"

    @allure.title("После окончания таймера отображается окно совершённого заказа по ТЗ")
    def test_order_completed_window_has_all_elements(self, order_page):
        order_page.select_tariff(TariffNames.WORKER)
        order_page.enable_laptop_table()
        order_page.click_order_button()
        order_page.wait_for_order_completed(timeout=60)
        header_text = order_page.get_order_header_text()
        assert (
            "приедет" in header_text
            and order_page.is_completed_order_window_visible()
        ), f"Окно совершённого заказа не соответствует ТЗ, заголовок: '{header_text}'"

    @allure.title("В деталях заказа отображается стоимость поездки")
    def test_details_shows_tariff_price(self, order_page):
        order_page.select_tariff(TariffNames.WORKER)
        order_page.enable_laptop_table()
        order_page.click_order_button()
        order_page.wait_for_order_completed(timeout=60)
        order_page.click_details()
        price_text = order_page.get_details_price_text()
        assert "Стоимость" in price_text and "₽" in price_text, \
            f"Стоимость не отображается в деталях: '{price_text}'"
        
    @allure.title("Кнопка Отмена закрывает окно заказа")
    def test_cancel_closes_order_window(self, order_page):
        order_page.select_tariff(TariffNames.WORKER)
        order_page.enable_laptop_table()
        order_page.click_order_button()
        order_page.click_cancel()
        assert order_page.is_order_window_closed(), \
            "Окно заказа не закрылось после нажатия Отмена"
