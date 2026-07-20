from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Тарифы
    TARIFF_CARDS = (By.CLASS_NAME, "tariff-cards")
    TARIFF_CARD = (By.CLASS_NAME, "tcard")
    TARIFF_CARD_ACTIVE = (By.XPATH, ".//div[contains(@class,'tcard active')]")
    TARIFF_CARD_TITLE = (By.CLASS_NAME, "tcard-title")
    TARIFF_I_BUTTON = (By.CLASS_NAME, "tcard-i")

    # Тариф Рабочий
    TARIFF_WORKER = (By.XPATH,
        ".//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='Рабочий']]")

    # Всплывающее окно описания тарифа
    TARIFF_POPUP = (By.XPATH, ".//div[contains(@class,'tariff-popup') or contains(@class,'tooltip')]")

    # Поля заказа
    INPUT_PHONE = (By.ID, "phone")
    INPUT_PAYMENT = (By.ID, "cash")
    INPUT_COMMENT = (By.ID, "comment")

    # Чекбокс Столик для ноутбука
    CHECKBOX_LAPTOP_TABLE = (By.XPATH,
        ".//div[contains(@class,'switch') and preceding-sibling::*[contains(text(),'Столик')]]"
        " | .//input[@class='switch-input']")

    # Кнопка заказа
    BUTTON_ORDER = (By.XPATH, ".//button[contains(text(),'Ввести номер и заказать')]")

    # Окно ожидания машины
    ORDER_HEADER_SEARCH = (By.XPATH, ".//div[contains(text(),'Поиск машины')]")
    ORDER_TIMER = (By.XPATH,
        ".//div[contains(@class,'order-timer') or contains(@class,'timer')]")
    BUTTON_CANCEL = (By.XPATH, ".//button[contains(@class,'order-button')]")
    BUTTON_DETAILS = (By.XPATH,
        "(.//button[contains(@class,'order-button')])[2]")

    # Окно совершённого заказа
    ORDER_HEADER_ARRIVED = (By.CLASS_NAME, "order-header-title")
    ORDER_NUMBER = (By.CLASS_NAME, "order-number")
    ORDER_DRIVER_RATING = (By.CLASS_NAME, "order-btn-rating")

    # Детали заказа
    ORDER_DETAILS = (By.CLASS_NAME, "order-details")
    ORDER_DETAILS_PRICE = (By.XPATH,
        ".//div[contains(@class,'order-details-content') and contains(text(),'Стоимость')]")