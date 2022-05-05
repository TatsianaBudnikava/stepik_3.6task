import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser")
    parser.addoption('--language', action='store', default='es',
                 help="Choose language: de, en, fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    

   
    