from selenium import webdriver
from data import Constants
import pytest
import requests
from faker import Faker
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

faker = Faker()


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    driver.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def user_data():
    payload = {
        'email': faker.email(),
        'password': faker.password(),
        'name': faker.name()
    }
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', json=payload)
    payload['token'] = response.json()['accessToken'].replace('Bearer ', '')
    return payload

@pytest.fixture(scope='class', autouse=True)
def delete_user(user_data):
    yield
    headers = {
        'Authorization': user_data['token']
    }
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)