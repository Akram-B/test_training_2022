from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    _driver = driver = webdriver.Chrome()
    yield _driver
    _driver.close()


def test_search_in_python_org(driver):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(by=By.NAME, value="q")
    elem.send_keys("pytest")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source


def test_fail_search_in_python_org(driver):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(by=By.NAME, value="q")
    elem.send_keys("should_not_exist")
    elem.send_keys(Keys.RETURN)
    assert "No results found." in driver.page_source