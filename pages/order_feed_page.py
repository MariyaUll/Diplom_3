import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from urls import ORDER_FEED_URL


class OrderFeedPage(BasePage):

    @allure.step("Открыть ленту заказов")
    def open_feed_page(self):
        self.open_url(ORDER_FEED_URL)

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_feed_loaded(self, timeout=10):
        self.find_visible_element(OrderFeedLocators.ORDERS_DATA_CONTAINER)

    @allure.step("Получить значение счётчика «Выполнено за всё время»")
    def get_total_counter(self):
        return self.get_text(OrderFeedLocators.TOTAL_COUNTER)

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_today_counter(self):
        return self.get_text(OrderFeedLocators.TODAY_COUNTER)

    @allure.step("Получить список номеров заказов «В работе»")
    def get_in_progress_orders(self):
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ITEMS)
        return [el.text.strip() for el in elements if el.text.strip()]

    @allure.step("Получить список номеров готовых заказов")
    def get_ready_orders(self, timeout=10):
        self.wait_for_condition(
            lambda _: self.find_elements(OrderFeedLocators.READY_ORDERS_ITEMS),
            timeout,
        )
        elements = self.find_elements(OrderFeedLocators.READY_ORDERS_ITEMS)
        return [el.text.strip() for el in elements]

    @allure.step("Дождаться появления заказа {order_number_with_zero} в разделе «В работе»")
    def wait_order_in_progress(self, order_number_with_zero, timeout=10):
        def order_in_progress(_):
            elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ITEMS)
            texts = [el.text.strip() for el in elements if el.text.strip()]
            return order_number_with_zero in texts

        return self.wait_for_condition(order_in_progress, timeout)

    @allure.step("Дождаться загрузки списка готовых заказов")
    def wait_ready_orders_loaded(self):
        self.wait_for_element_to_disappear(OrderFeedLocators.READY_ORDERS_PLACEHOLDER)
