import allure

from data import RouteModes, TransportTypes


@allure.feature("Подготовка к заказу такси")
class TestTaxiPreparation:
    @allure.title("Переключение Оптимальный/Быстрый меняет таб и пересчитывает время и стоимость")
    def test_switching_modes_recalculates_route(self, route_set):
        route_set.click_mode_optimal()
        optimal_mode = route_set.get_active_mode()
        optimal_price = route_set.get_route_price()
        optimal_duration = route_set.get_route_duration()

        route_set.click_mode_fast()
        fast_mode = route_set.get_active_mode()
        fast_price = route_set.get_route_price()
        fast_duration = route_set.get_route_duration()

        assert (
            optimal_mode == RouteModes.OPTIMAL
            and fast_mode == RouteModes.FAST
            and (optimal_price != fast_price or optimal_duration != fast_duration)
        ), (
            f"Таб или расчёт маршрута не изменились: "
            f"режимы {optimal_mode}/{fast_mode}, "
            f"цены {optimal_price}/{fast_price}, "
            f"время {optimal_duration}/{fast_duration}"
        )

    @allure.title("При выборе 'Свой' становятся активны все типы передвижения")
    def test_custom_mode_shows_transport_types(self, route_set):
        route_set.click_mode_custom()
        transport_types = route_set.get_transport_types()
        missing = [t for t in TransportTypes.ALL if t not in transport_types]
        assert route_set.get_active_mode() == RouteModes.CUSTOM and not missing, \
            f"Таб 'Свой' не активен или отсутствуют типы передвижения: {missing}"

    @allure.title("При выборе 'Быстрый' активна кнопка 'Вызвать такси'")
    def test_fast_mode_shows_call_taxi_button(self, route_set):
        route_set.click_mode_fast()
        assert route_set.is_call_taxi_button_visible(), \
            "Кнопка 'Вызвать такси' не отображается"

    @allure.title("При выборе 'Свой' и типа 'Драйв' активна кнопка 'Забронировать'")
    def test_custom_drive_shows_book_button(self, route_set):
        route_set.click_mode_custom()
        route_set.select_transport_type(TransportTypes.DRIVE)
        assert route_set.is_book_drive_button_visible(), \
            "Кнопка 'Забронировать' не отображается"
