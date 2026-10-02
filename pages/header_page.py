import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from urls import MAIN_PAGE_URL, ORDER_FEED_URL


class HeaderPage(BasePage):

    @allure.step("Кликнуть на «Конструктор»")
    def click_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)

    @allure.step("Кликнуть на «Лента Заказов»")
    def click_order_feed(self):
        self.click(HeaderLocators.ORDER_FEED_LINK)

    @allure.step("Кликнуть на «Личный Кабинет»")
    def click_personal_account(self):
        self.click(HeaderLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Проверить переход на главную страницу")
    def is_main_page(self):
        self.wait_for_url(MAIN_PAGE_URL)
        return self.get_current_url() == MAIN_PAGE_URL

    @allure.step("Проверить переход в ленту заказов")
    def is_order_feed_page(self):
        self.wait_for_url(ORDER_FEED_URL)
        return self.get_current_url() == ORDER_FEED_URL
