from pytest import fixture

from selenium import webdriver


@fixture(scope='function')  # can be also session if we want one instance of the webdriver for all tests
def chrome_browser():
    browser = webdriver.Chrome()
    return browser
