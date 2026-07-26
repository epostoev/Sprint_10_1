# Sprint_n — UI-тесты для Яндекс.Маршруты

UI-автотесты для учебного сервиса [Яндекс.Маршруты](https://qa-routes.education-services.ru/).  
Покрыты сценарии отрисовки маршрута, выбора вида маршрута, подготовки к заказу и полного флоу заказа такси.

## Список реализованных тестов

### 🗺️ Отрисовка маршрута (`TestRouteDrawing`)

| Тест | Описание |
|:---|:---|
| `test_two_point_visible_for_different_addresses` | При вводе двух разных адресов на карте отображаются две точки маршрута. |

### 🧭 Отрисовка блока с выбором маршрута (`TestRouteBlock`)

| Тест | Описание |
|:---|:---|
| `test_modes_block_visible_for_different_addresses` | При вводе двух разных адресов отображается блок выбора маршрута. |
| `test_same_address_shows_free_route_block` | При вводе одинакового адреса отображается блок «Авто Бесплатно В пути 0 мин.». |

### 🚕 Подготовка к заказу такси (`TestTaxiPreparation`)

| Тест | Описание |
|:---|:---|
| `test_switching_modes_recalculates_route` | Переключение Оптимальный/Быстрый меняет активный таб и пересчитывает время и стоимость. |
| `test_custom_mode_shows_transport_types` | При выборе «Свой» становятся активны все типы передвижения. |
| `test_fast_mode_shows_call_taxi_button` | При выборе «Быстрый» активна кнопка «Вызвать такси». |
| `test_custom_drive_shows_book_button` | При выборе «Свой» + «Драйв» активна кнопка «Забронировать». |

### 💰 Заказ тарифа Такси (`TestTaxiOrder`)

| Тест | Описание |
|:---|:---|
| `test_order_form_has_six_tariffs_one_active` | Форма заказа содержит все 6 тарифов, один активный. |
| `test_worker_tariff_description` | Описание тарифа «Рабочий» соответствует ТЗ. |
| `test_sleepy_tariff_description` | Описание тарифа «Сонный» соответствует ТЗ. |
| `test_vacation_tariff_description` | Описание тарифа «Отпускной» соответствует ТЗ. |
| `test_talkative_tariff_description` | Описание тарифа «Разговорчивый» соответствует ТЗ. |
| `test_comfort_tariff_description` | Описание тарифа «Утешительный» соответствует ТЗ. |
| `test_glossy_tariff_description` | Описание тарифа «Глянцевый» соответствует ТЗ. |
| `test_order_fields_visible_below_tariffs` | Под тарифами отображаются поля Телефон, Способ оплаты, Комментарий. |

### 🏁 Заказ тарифа Такси — полный флоу (`TestTaxiOrderFlow`)

| Тест | Описание |
|:---|:---|
| `test_search_window_has_all_elements` | После заказа отображается окно ожидания машины со всеми элементами. |
| `test_order_completed_window_has_all_elements` | После окончания таймера отображается окно совершённого заказа. |
| `test_details_shows_tariff_price` | После клика на «Детали» отображается стоимость поездки. |
| `test_cancel_closes_order_window` | Кнопка «Отмена» закрывает окно заказа. |

---

## 🛠 Технические особенности

- **Page Object Model** — каждая страница описана отдельным классом в `pages/`, общие методы в `BasePage`.
- **Локаторы** — вынесены в пакет `locators/`, по файлу на страницу.
- **Тестовые данные** — в `data.py` (адреса, режимы, типы транспорта, тарифы и их описания).
- **Фикстуры** — цепочка `driver` → `main_page` → `route_set` → `fast_route` → `taxi_order_form` → `order_page` для предусловий.
- **hover** — наведение курсора реализовано через `ActionChains.move_to_element`.
- **Allure-отчёты** — размечены `@allure.feature`, `@allure.title`, шаги — `@allure.step`.

---

## 🚀 Запуск

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск всех тестов
```bash
pytest -v
```

### Запуск через Makefile
```bash
make test              # запуск тестов с генерацией allure-results
make report            # открыть Allure-отчёт в браузере
make report-generate   # сгенерировать папку allure-report
```

### Запуск с Allure-отчётом вручную
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 📁 Структура проекта

```
Sprint_n/
├── locators/
│   ├── main_page_locators.py
│   └── order_page_locators.py
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
├── tests/
│   ├── test_route_drawing.py
│   ├── test_route_block.py
│   ├── test_taxi_preparation.py
│   └── test_taxi_order.py
├── conftest.py
├── data.py
├── pytest.ini
├── Makefile
└── requirements.txt
```