import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help='Choose language for browser')


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption('language')
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})

        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", lang)

        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(15)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

