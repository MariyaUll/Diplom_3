from selenium.webdriver.common.by import By


class OrderFeedLocators:
    TOTAL_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за все время')]"
        "/following-sibling::p[contains(@class, 'OrderFeed_number')]",
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за сегодня')]"
        "/following-sibling::p[contains(@class, 'OrderFeed_number')]",
    )

    ORDERS_DATA_CONTAINER = (
        By.CSS_SELECTOR,
        "div[class*='OrderFeed_ordersData']",
    )

    IN_PROGRESS_ITEMS = (
        By.CSS_SELECTOR,
        "ul[class*='OrderFeed_orderListReady'] li",
    )
    READY_ORDERS_ITEMS = (
        By.CSS_SELECTOR,
        "ul[class*='OrderFeed_orderListReady'] li",
    )
    READY_ORDERS_PLACEHOLDER = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]"
        "//li[contains(text(), 'Все текущие заказы готовы')]",
    )
