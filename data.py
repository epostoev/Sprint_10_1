class URLS:
    BASE_URL = "https://qa-routes.education-services.ru/"


class Addresses:
    FROM_ADDRESS = "Хамовнический вал, 34"
    TO_ADDRESS = "Зубовский бульвар, 37"
    SAME_ADDRESS = "Хамовнический вал, 34"


class TariffNames:
    WORKER = "Рабочий"
    SLEEPY = "Сонный"
    VACATION = "Отпускной"
    TALKATIVE = "Разговорчивый"
    COMFORT = "Утешительный"
    GLOSSY = "Глянцевый"
    ALL = [WORKER, SLEEPY, VACATION, TALKATIVE, COMFORT, GLOSSY]


class TariffDescriptions:
    WORKER = "Для деловых особ, которых отвлекают"
    SLEEPY = "Если мысли не выходят из головы"
    VACATION = "Если пришла пора отдохнуть"
    TALKATIVE = "Для тех, кто не выспался"
    COMFORT = "Если хочется свернуться калачиком"
    GLOSSY = "Если нужно блистать"


class RouteModes:
    OPTIMAL = "Оптимальный"
    FAST = "Быстрый"
    CUSTOM = "Свой"


class TransportTypes:
    CAR = "car"
    WALK = "walk"
    TAXI = "taxi"
    BIKE = "bike"
    SCOOTER = "scooter"
    DRIVE = "drive"
    ALL = [CAR, WALK, TAXI, BIKE, SCOOTER, DRIVE]
