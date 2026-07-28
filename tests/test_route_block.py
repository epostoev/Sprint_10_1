import allure

from data import Addresses


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteBlock:

    @allure.title("При вводе двух разных адресов отображается блок выбора маршрута")
    def test_modes_block_visible_for_different_addresses(self, main_page):
        with allure.step("Вводим два разных адреса 'Откуда' и 'Куда'"):
            main_page.set_route(Addresses.FROM_ADDRESS, Addresses.TO_ADDRESS)
        with allure.step("Проверяем что отображается блок выбора маршрута"):
            assert main_page.is_modes_container_visible(), \
                "Блок выбора маршрута не отображается"

    @allure.title("При вводе одинакового адреса отображается блок 'Авто Бесплатно В пути 0 мин.'")
    def test_same_address_shows_free_route_block(self, main_page):
        with allure.step("Вводим одинаковый адрес в 'Откуда' и 'Куда'"):
            main_page.set_route(Addresses.SAME_ADDRESS, Addresses.SAME_ADDRESS)
        with allure.step("Проверяем что отображается блок с бесплатным маршрутом"):
            assert main_page.is_same_address_block_correct(), \
                "Блок не содержит ожидаемый текст 'Авто Бесплатно В пути 0 мин.'"