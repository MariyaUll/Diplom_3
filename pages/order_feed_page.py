import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from urls import ORDER_FEED_URL


class OrderFeedPage(BasePage):

    @allure.step("Открыть ленту заказов")
    def open_feed_page(self):
        self.open_url(ORDER_FEED_URL)

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_feed_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(OrderFeedLocators.ORDERS_DATA_CONTAINER)
        )

    @allure.step("Получить значение счётчика «Выполнено за всё время»")
    def get_total_counter(self):
        return self.get_text(OrderFeedLocators.TOTAL_COUNTER)

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_today_counter(self):
        return self.get_text(OrderFeedLocators.TODAY_COUNTER)

    @allure.step("Получить список номеров заказов «В работе»")
    def get_in_progress_orders(self):
        elements = self.driver.find_elements(*OrderFeedLocators.IN_PROGRESS_ITEMS)
        return [el.text.strip() for el in elements if el.text.strip()]

    def get_ready_orders(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_elements(*OrderFeedLocators.READY_ORDERS_ITEMS)
        )
        elements = self.driver.find_elements(*OrderFeedLocators.READY_ORDERS_ITEMS)
        return [el.text.strip() for el in elements]

    def wait_order_in_progress(self, order_number_with_zero, timeout=10):
        """Ждёт, пока заказ появится в секции 'В работе'."""
        def order_in_progress(driver):
            elements = driver.find_elements(*OrderFeedLocators.IN_PROGRESS_ITEMS)
            texts = [el.text.strip() for el in elements if el.text.strip()]
            return order_number_with_zero in texts

        return WebDriverWait(self.driver, timeout).until(order_in_progress)

    def wait_ready_orders_loaded(self, timeout=10):
        """Ждёт, пока пропадёт заглушка 'Все текущие заказы готовы!'."""
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(OrderFeedLocators.READY_ORDERS_PLACEHOLDER)
        )
