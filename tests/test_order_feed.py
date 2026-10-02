import allure
from pages.order_feed_page import OrderFeedPage
from helpers.order_helper import OrderHelper


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Увеличение счётчика «Выполнено за всё время»")
    @allure.description("Проверка, что счётчик «Выполнено за всё время» увеличивается после создания заказа")
    def test_completed_all_time_counter_increases(self, driver):
        feed_page = OrderFeedPage(driver)

        feed_page.open_feed_page()
        feed_page.wait_feed_loaded()
        counter_before = feed_page.get_total_counter()

        helper = OrderHelper()
        helper.create_order(driver)

        feed_page.open_feed_page()
        feed_page.wait_feed_loaded()
        counter_after = feed_page.get_total_counter()

        assert int(counter_after) > int(counter_before)

    @allure.title("Увеличение счётчика «Выполнено за сегодня»")
    @allure.description("Проверка, что счётчик «Выполнено за сегодня» увеличивается после создания заказа")
    def test_completed_today_counter_increases(self, driver):
        feed_page = OrderFeedPage(driver)

        feed_page.open_feed_page()
        feed_page.wait_feed_loaded()
        counter_before = feed_page.get_today_counter()

        helper = OrderHelper()
        helper.create_order(driver)

        feed_page.open_feed_page()
        feed_page.wait_feed_loaded()
        counter_after = feed_page.get_today_counter()

        assert int(counter_after) > int(counter_before)

    @allure.title("Появление номера заказа в разделе «В работе»")
    @allure.description("Проверка, что после оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_progress(self, driver):
        feed_page = OrderFeedPage(driver)

        feed_page.open_feed_page()
        feed_page.wait_feed_loaded()

        helper = OrderHelper()
        order_number = helper.create_order(driver)
        order_number_with_zero = f"0{order_number}"

        feed_page.open_feed_page()
        feed_page.wait_feed_loaded()
        feed_page.wait_ready_orders_loaded()

        in_progress_orders = feed_page.get_in_progress_orders()

        assert order_number_with_zero in in_progress_orders
