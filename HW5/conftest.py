import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_manager():
    # Установка размера окна браузера
    browser.config.window_width = 1920
    browser.config.window_height = 1020

    yield

    # Завершение работы браузера после выполнения тестов
    browser.quit()

