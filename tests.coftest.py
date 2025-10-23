import pytest
from selenium import webdriver
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://vut-frontend.tcdev.site/auth/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
