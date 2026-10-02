from selenium.webdriver.common.by import By


class HeaderLocators:
    """Локаторы элементов шапки приложения."""
    CONSTRUCTOR_LINK = (By.CSS_SELECTOR, "a[href='/']")
    ORDER_FEED_LINK = (By.CSS_SELECTOR, "a[href='/feed']")
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/account']")