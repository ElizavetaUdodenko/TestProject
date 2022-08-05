import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose the browse: chrome or firefox')
    parser.addoption('--language', action='store', default='en', help='Choose the language')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    print('Start browser')
    browser = None
    user_language = request.config.getoption('language')
    print(f'Used language: {user_language}')
    if browser_name == 'chrome':
        print('New Chrome window')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('New Firefox window')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('Close browser')
    browser.quit()

