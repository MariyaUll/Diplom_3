import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import LOGIN_PAGE_URL, REGISTER_PAGE_URL


class LoginPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open_url(LOGIN_PAGE_URL)

    @allure.step("Открыть страницу регистрации")
    def open_register_page(self):
        self.open_url(REGISTER_PAGE_URL)

    @allure.step("Дождаться загрузки страницы входа")
    def wait_login_page_loaded(self):
        self.find_visible_element(LoginPageLocators.LOGIN_PAGE_TITLE)

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Ввести имя: {name}")
    def enter_name(self, name):
        self.send_keys(LoginPageLocators.NAME_INPUT, name)

    @allure.step("Кликнуть кнопку «Войти»")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Кликнуть кнопку «Зарегистрироваться»")
    def click_register_button(self):
        self.click(LoginPageLocators.REGISTER_BUTTON)

    @allure.step("Залогиниться с email={email}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Зарегистрироваться: name={name}, email={email}")
    def register(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register_button()
