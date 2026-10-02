import allure
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Открытие модального окна с деталями ингредиента")
    @allure.description("Проверка появления всплывающего окна при клике на ингредиент")
    def test_ingredient_modal_opens_on_click(self, driver):
        main_page = MainPage(driver)
        main_page.wait_constructor_loaded()
        main_page.click_first_ingredient()
        main_page.wait_ingredient_modal_opened()

        assert main_page.is_ingredient_modal_opened()

    @allure.title("Закрытие модального окна кликом по крестику")
    @allure.description("Проверка закрытия всплывающего окна кликом по крестику")
    def test_ingredient_modal_closes_by_cross_click(self, driver):
        main_page = MainPage(driver)
        main_page.wait_constructor_loaded()
        main_page.click_first_ingredient()
        main_page.wait_ingredient_modal_opened()
        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_closed()

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    @allure.description("Проверка, что счётчик ингредиента увеличивается после перетаскивания в конструктор")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        counter_before = main_page.get_first_ingredient_counter()
        main_page.drag_first_ingredient_to_constructor()
        counter_after = main_page.get_first_ingredient_counter()

        assert int(counter_after) > int(counter_before)
