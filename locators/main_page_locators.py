from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//h1[contains(text(), 'Соберите бургер')]",
    )

    FIRST_INGREDIENT = (
        By.CSS_SELECTOR,
        '[class^="BurgerIngredients_ingredients__menuContainer"] ul:first-of-type a',
    )
    INGREDIENT_COUNTER = (
        By.CSS_SELECTOR,
        '[class^="BurgerIngredients_ingredients__menuContainer"] ul:first-of-type a [class^="counter"]',
    )
    BASKET_LIST = (
        By.CSS_SELECTOR,
        '[class^="BurgerConstructor_basket__list"]',
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
