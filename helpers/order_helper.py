import allure
import faker

fake = faker.Faker()

@allure.step("Сгенерировать уникальные данные пользователя")
def generate_user_data():
    """Генерирует уникальные данные пользователя."""
    return {
        "email": fake.email(),
        "password": fake.password(length=8),
        "name": fake.name(),
    }

class OrderHelper:
    @allure.step("Создать заказ")
    def create_order(self, login_page, main_page):
        """Регистрирует пользователя, логинится, оформляет заказ. Возвращает номер заказа."""
        user_data = generate_user_data()

        login_page.open_register_page()
        login_page.register(
            user_data["name"], user_data["email"], user_data["password"]
        )

        login_page.open_login_page()
        login_page.wait_login_page_loaded()
        login_page.login(user_data["email"], user_data["password"])

        main_page.wait_constructor_loaded()
        main_page.drag_first_ingredient_to_constructor()
        main_page.click_place_order()
        main_page.wait_order_modal_opened()

        order_number = main_page.get_order_number()
        main_page.close_order_modal()

        return order_number
