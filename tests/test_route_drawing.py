import allure

from data import Addresses


@allure.feature("Отрисовка маршрута")
class TestRouteDrawing:

    @allure.title("При вводе двух разных адресов на карте отображаются две точки маршрута")
    def test_two_pins_visible_for_different_addresses(self, main_page):
        with allure.step("Вводим два разных адреса 'Откуда' и 'Куда'"):
            main_page.set_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        with allure.step("Проверяем что на карте отображаются две точки маршрута"):
            assert main_page.are_route_pins_visible(), \
                "На карте не отображаются две точки маршрута"