import allure
from pages.header_page import HeaderPage
from urls import MAIN_PAGE_URL, ORDER_FEED_URL


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Проверка перехода на главную страницу по клику на «Конструктор»")
    def test_go_to_constructor_by_click(self, driver):
        header = HeaderPage(driver)
        header.click_order_feed()
        header.wait_for_url(ORDER_FEED_URL)

        header.click_constructor()
        header.wait_for_url(MAIN_PAGE_URL)

        assert driver.current_url == MAIN_PAGE_URL

    @allure.title("Переход по клику на «Лента Заказов»")
    @allure.description("Проверка перехода в ленту заказов по клику на «Лента Заказов»")
    def test_go_to_order_feed_by_click(self, driver):
        header = HeaderPage(driver)
        header.click_order_feed()
        header.wait_for_url(ORDER_FEED_URL)

        assert driver.current_url == ORDER_FEED_URL
