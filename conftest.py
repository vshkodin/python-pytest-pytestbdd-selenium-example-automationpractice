import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromepath=r'C:\tools\chromedriver.exe'

def pytest_addoption(parser):
    parser.addoption('--headless', action='store', default="false", dest='headless')


@pytest.fixture(scope='session')
def init_driver(request):
    options = Options()
    if request.config.getoption('headless')=='true':
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=chromepath)
        driver.implicitly_wait(25)
    else:
        driver = webdriver.Chrome(options=options, executable_path=chromepath)
        driver.implicitly_wait(25)

    driver.get("http://automationpractice.com/index.php")
    yield driver
    driver.quit()