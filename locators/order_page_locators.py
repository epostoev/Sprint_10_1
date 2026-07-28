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

    # Всплывающее окно описания тарифа — появляется при наведении на кнопку i
    # Некоторые попапы не получают класс show, ищем по visible стилю
    TARIFF_POPUP = (By.XPATH,
        ".//div[contains(@class,'i-floating-tooltip') and contains(@class,'show')]"
        " | .//div[contains(@class,'i-floating-tooltip') and not(contains(@style,'display: none'))]")
    TARIFF_POPUP_DESCRIPTION = (By.XPATH,
        "(.//div[contains(@class,'i-floating-tooltip')]//div[@class='i-dPrefix'])[last()]")

    # Поля заказа — блоки под тарифами
    FIELD_PHONE = (By.XPATH, ".//div[@class='np-text' and text()='Телефон']")
    FIELD_PAYMENT = (By.XPATH, ".//div[@class='pp-text' and text()='Способ оплаты']")
    FIELD_COMMENT = (By.XPATH, ".//input[@id='comment']")
    FIELD_REQUIREMENTS = (By.XPATH, ".//div[contains(@class,'reqs')]")

    # Блок «Требования к заказу»
    REQUIREMENTS_HEADER = (By.CLASS_NAME, "reqs-header")
    REQUIREMENTS_BODY = (By.CLASS_NAME, "reqs-body")

    # Чекбокс «Столик для ноутбука» — кликаем по слайдеру, input скрыт
    CHECKBOX_LAPTOP_TABLE = (By.XPATH,
        ".//div[@class='r-sw-container'][div[text()='Столик для ноутбука']]//span[@class='slider round']")
    CHECKBOX_LAPTOP_TABLE_INPUT = (By.XPATH,
        ".//div[@class='r-sw-container'][div[text()='Столик для ноутбука']]//input[@class='switch-input']")

    # Кнопка заказа
    BUTTON_ORDER = (By.XPATH, ".//button[contains(@class,'smart-button')]")

    # Окно заказа (общее)
    ORDER_WINDOW = (By.XPATH, ".//div[contains(@class,'order') and contains(@class,'shown')]")
    ORDER_HEADER_TITLE = (By.CLASS_NAME, "order-header-title")
    ORDER_TIMER = (By.CLASS_NAME, "order-header-time")

    # Кнопки окна заказа
    BUTTON_CANCEL = (By.XPATH,
        ".//div[@class='order-btn-group'][div[text()='Отменить']]//button")
    BUTTON_DETAILS = (By.XPATH,
        ".//div[@class='order-btn-group'][div[text()='Детали']]//button")

    # Окно совершённого заказа
    ORDER_NUMBER = (By.CLASS_NAME, "order-number")
    ORDER_DRIVER_RATING = (By.CLASS_NAME, "order-btn-rating")

    # Детали заказа
    ORDER_DETAILS = (By.CLASS_NAME, "order-details")
    ORDER_DETAILS_ROW = (By.CLASS_NAME, "order-details-row")
    ORDER_DETAILS_PRICE = (By.XPATH,
        ".//div[@class='order-details-row'][.//div[contains(text(),'Еще про поездку')]]"
        "//div[@class='o-d-sh']")

    TARIFF_POPUP_DESCRIPTION = (By.XPATH, ".//div[@class='i-dPrefix']")