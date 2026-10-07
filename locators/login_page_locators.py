from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы страницы авторизации и регистрации."""
    # Поля формы входа
    EMAIL_INPUT = (
        By.XPATH,
        "//label[contains(text(), 'Email')]/following-sibling::input",
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(text(), 'Пароль')]/following-sibling::input",
    )
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти')]",
    )

    # Поля формы регистрации
    NAME_INPUT = (
        By.XPATH,
        "//label[contains(text(), 'Имя')]/following-sibling::input",
    )
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Зарегистрироваться')]",
    )

    # Ссылки
    REGISTER_LINK = (
        By.XPATH,
        "//a[contains(text(), 'Зарегистрироваться')]",
    )

    # Заголовок страницы входа
    LOGIN_PAGE_TITLE = (
        By.XPATH,
        "//h2[contains(text(), 'Вход')]",
    )
