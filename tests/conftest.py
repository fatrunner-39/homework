from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    selenium_grid_url = "http://172.17.0.1:4444"

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=selenium_grid_url, options=chrome_options)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def fibonacci():
    day = datetime.today().day
    n = int(day)

    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return b


