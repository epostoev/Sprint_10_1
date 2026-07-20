from selenium.webdriver.common.by import By


class MainPageLocators:
    # Поля адресов
    INPUT_FROM = (By.ID, "from")
    INPUT_TO = (By.ID, "to")

    # Точки маршрута на карте
    ROUTE_PINS = (By.XPATH, ".//ymaps[contains(@class,'ymaps-2-1-79-route-pin_state_expanded')]")

    # Блок с выбором маршрута
    MODES_CONTAINER = (By.CLASS_NAME, "modes-container")
    MODE_OPTIMAL = (By.XPATH, ".//div[@class='mode' and text()='Оптимальный']")
    MODE_FAST = (By.XPATH, ".//div[contains(@class,'mode') and text()='Быстрый']")
    MODE_CUSTOM = (By.XPATH, ".//div[@class='mode' and text()='Свой']")
    MODE_ACTIVE = (By.XPATH, ".//div[contains(@class,'mode active')]")

    # Блок результатов при одинаковом адресе
    SAME_ADDRESS_TEXT = (By.CLASS_NAME, "results-text")
    SAME_ADDRESS_AUTO = (By.XPATH, ".//div[contains(@class,'text') and contains(text(),'Авто')]")
    SAME_ADDRESS_DURATION = (By.CLASS_NAME, "duration")

    # Типы передвижения (для режима Свой)
    TRANSPORT_TYPES = (By.XPATH, ".//div[@class='types-container']//div[@class='mode']")

    # Кнопка Вызвать такси
    BUTTON_CALL_TAXI = (By.XPATH, ".//button[contains(@class,'round') and text()='Вызвать такси']")

    # Кнопка Забронировать (Драйв)
    BUTTON_BOOK_DRIVE = (By.XPATH, ".//button[contains(text(),'Забронировать')]")