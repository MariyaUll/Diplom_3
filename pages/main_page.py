import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_url(MAIN_PAGE_URL)

    @allure.step("Дождаться загрузки конструктора")
    def wait_constructor_loaded(self):
        self.find_visible_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Дождаться открытия модального окна ингредиента")
    def wait_ingredient_modal_opened(self):
        self.find_visible_element(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Проверить, что модальное окно ингредиента открыто")
    def is_ingredient_modal_opened(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.close_modal(
            MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON,
            MainPageLocators.INGREDIENT_MODAL,
        )

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_closed(self):
        return not self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Получить значение счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        element = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_COUNTER)
        )
        return element.text

    @allure.step("Перетащить первый ингредиент в конструктор")
    def drag_first_ingredient_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.FIRST_INGREDIENT,
            MainPageLocators.BASKET_LIST,
        )


    @allure.step("Кликнуть «Оформить заказ»")
    def click_place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Дождаться открытия окна с номером заказа")
    def wait_order_modal_opened(self):
        self.find_visible_element(MainPageLocators.ORDER_MODAL)

    def get_order_number(self, timeout=10):
        def order_number_ready(driver):
            elements = driver.find_elements(*MainPageLocators.ORDER_NUMBER)
            if not elements:
                return False
            text = elements[0].text.strip()
            if text and text != "9999":
                return elements[0]
            return False

        element = WebDriverWait(self.driver, timeout).until(order_number_ready)
        return element.text.strip()

    @allure.step("Закрыть модальное окно с номером заказа")
    def close_order_modal(self):
        self.close_modal(
            MainPageLocators.ORDER_MODAL_CLOSE_BUTTON,
            MainPageLocators.ORDER_MODAL,
        )

    @allure.step("Кликнуть «Войти в аккаунт»")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)
