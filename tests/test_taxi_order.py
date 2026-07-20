import allure


@allure.feature("Отрисовка маршрута")
class TestRouteDrawing:
    @allure.title("При вводе двуз разных адресов на карте отображаются две точки маршрута")
    def test_two_point_visible_for_different_addresses(self, route_set):
        assert route_set.are_route_pins_visible(), \
            "На карте не отображаются две точки маршрута"
