import json

from pytest import fixture
from random import *


from selenium import webdriver


data_path = r'.\tests\test_data.json'


@fixture(scope='function')  # can be also session if we want one instance of the webdriver for all tests
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    print('Test')


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    pass


@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield driver
    drvr.quit()


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(data_path))
def test_data(request):
    data = request.param
