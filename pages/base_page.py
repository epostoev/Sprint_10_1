import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Вводим текст в поле")
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Кликаем по элементу")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def find_child_element(self, parent, locator):
        """Находит дочерний элемент внутри родительского."""
        return parent.find_element(*locator)

    def wait_for_element_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator))

    def wait_for_text_in_element(self, locator, text, timeout=60):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text))

    def wait_until(self, condition, timeout=15):
        """Универсальное ожидание произвольного условия."""
        return WebDriverWait(self.driver, timeout).until(condition)

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def count_visible_elements(self, locator):
        """Возвращает количество видимых элементов по локатору."""
        return len([e for e in self.driver.find_elements(*locator) if e.is_displayed()])

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_inner_text(self, element):
        """Возвращает innerText элемента через JS (видит текст вне viewport)."""
        return self.driver.execute_script("return arguments[0].innerText;", element)

    def get_element_attribute(self, locator, attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

    @allure.step("Наводим курсор на элемент")
    def hover_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("JS-клик по элементу")
    def click_js(self, locator):
        """Кликает по элементу через JavaScript (для перекрытых/скрытых элементов)."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)