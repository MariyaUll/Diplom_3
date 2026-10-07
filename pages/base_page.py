import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)

class BasePage:
    """Базовый класс для всех Page Object страниц."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти видимый элемент {locator}")
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти все элементы {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле {locator}")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_for_element_to_disappear(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться изменения URL на {url}")
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step("Перетаскивание элемента {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.element_to_be_clickable(source_locator))
        target = self.wait.until(EC.element_to_be_clickable(target_locator))
        self._execute_drag_and_drop_js(source, target)


    @allure.step("Выполнить drag-and-drop через JS: {source} → {target}")
    def _execute_drag_and_drop_js(self, source, target):
        js_script = """
        var source = arguments[0];
        var target = arguments[1];

        function createEvent(type) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(type, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function(key, val) { this.data[key] = val; },
                getData: function(key) { return this.data[key]; },
                clearData: function() { this.data = {}; },
                setDragImage: function() {},
                types: [],
                effectAllowed: 'all',
                dropEffect: 'move'
            };
            return event;
        }

        var dragStart = createEvent("dragstart");
        source.dispatchEvent(dragStart);

        var dragEnter = createEvent("dragenter");
        target.dispatchEvent(dragEnter);

        var dragOver = createEvent("dragover");
        target.dispatchEvent(dragOver);

        var drop = createEvent("drop");
        target.dispatchEvent(drop);

        var dragEnd = createEvent("dragend");
        source.dispatchEvent(dragEnd);
        """
        self.driver.execute_script(js_script, source, target)

    @allure.step("Закрыть модальное окно")
    def close_modal(self, close_locator, modal_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(close_locator))
            element.click()
        except ElementClickInterceptedException:
            element = self.driver.find_element(*close_locator)
            self.driver.execute_script("arguments[0].click();", element)
        self.wait_for_element_to_disappear(modal_locator)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Открыть страницу {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Дождаться выполнения условия")
    def wait_for_condition(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)
