import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.order_feed_page import OrderFeedPage
from helpers.order_helper import OrderHelper
from urls import MAIN_PAGE_URL


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests: chrome or firefox",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.set_window_size(1920, 1080)
    driver.get(MAIN_PAGE_URL)

    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.wait_constructor_loaded()
    return page


@pytest.fixture
def header_page(driver):
    return HeaderPage(driver)


@pytest.fixture
def order_feed_page(driver):
    page = OrderFeedPage(driver)
    page.open_feed_page()
    page.wait_feed_loaded()
    return page


# --- Фикстуры предусловий ---

@pytest.fixture
def ingredient_modal_opened(main_page):
    """Открывает модальное окно ингредиента — предусловие для тестов модалки."""
    main_page.click_first_ingredient()
    main_page.wait_ingredient_modal_opened()
    return main_page


@pytest.fixture
def on_order_feed_page(header_page):
    """Переходит в ленту заказов — предусловие для тестов навигации."""
    from urls import ORDER_FEED_URL
    header_page.click_order_feed()
    header_page.wait_for_url(ORDER_FEED_URL)
    return header_page

@pytest.fixture
def feed_page(driver):
    """Готовая страница ленты заказов (открыта и загружена)."""
    page = OrderFeedPage(driver)
    page.open_feed_page()
    page.wait_feed_loaded()
    return page

@pytest.fixture
def created_order_number(driver):
    """Создаёт заказ через Helper и возвращает номер заказа (без ведущего нуля)."""
    helper = OrderHelper()
    order_number = helper.create_order(driver)
    return order_number