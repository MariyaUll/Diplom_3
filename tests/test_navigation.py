import allure
from urls import MAIN_PAGE_URL, ORDER_FEED_URL


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Проверка перехода на главную страницу по клику на «Конструктор»")
    def test_go_to_constructor_by_click(self, on_order_feed_page):
        on_order_feed_page.click_constructor()
        on_order_feed_page.wait_for_url(MAIN_PAGE_URL)

        assert on_order_feed_page.get_current_url() == MAIN_PAGE_URL

    @allure.title("Переход по клику на «Лента Заказов»")
    @allure.description("Проверка перехода в ленту заказов по клику на «Лента Заказов»")
    def test_go_to_order_feed_by_click(self, on_order_feed_page):
        assert on_order_feed_page.get_current_url() == ORDER_FEED_URL
