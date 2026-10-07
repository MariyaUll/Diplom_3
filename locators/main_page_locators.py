from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//h1[contains(text(), 'Соберите бургер')]",
    )

    FIRST_INGREDIENT = (
        By.XPATH,
        "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']",
    )
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']"
        "//*[contains(@class, 'counter_counter__num')]",
    )
    BASKET_LIST = (
        By.CSS_SELECTOR,
        "[class^='BurgerConstructor_basket__list']",
    )

    INGREDIENT_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]",
    )
    INGREDIENT_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]",
    )

    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Оформить заказ')]",
    )

    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title')]",
    )
    ORDER_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]",
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти в аккаунт')]",
    )
