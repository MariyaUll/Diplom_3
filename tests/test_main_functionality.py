import allure


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Открытие модального окна с деталями ингредиента")
    @allure.description("Проверка появления всплывающего окна при клике на ингредиент")
    def test_ingredient_modal_opens_on_click(self, ingredient_modal_opened):
        assert ingredient_modal_opened.is_ingredient_modal_opened()

    @allure.title("Закрытие модального окна кликом по крестику")
    @allure.description("Проверка закрытия всплывающего окна кликом по крестику")
    def test_ingredient_modal_closes_by_cross_click(self, ingredient_modal_opened):
        ingredient_modal_opened.close_ingredient_modal()

        assert ingredient_modal_opened.is_ingredient_modal_closed()

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    @allure.description("Проверка, что счётчик ингредиента увеличивается после перетаскивания в конструктор")
    def test_ingredient_counter_increases(self, main_page):
        counter_before = main_page.get_first_ingredient_counter()
        main_page.drag_first_ingredient_to_constructor()
        counter_after = main_page.get_first_ingredient_counter()

        assert int(counter_after) > int(counter_before)
