import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--executor", action="store", default="http://192.168.31.89:4444/wd/hub", help="local or use selenoid"
    )
    parser.addoption(
        "--browser", default="chrome", help="browser to open"
    )
    parser.addoption(
        "--drivers_source", default="C:\selenium_drivers", help="Source where drivers exists"
    )
    parser.addoption(
        "--headless", action="store_true", help="browser to open"
    )
    parser.addoption(
        "--base_url", default="http://192.168.31.89:8081/", help="Service url"
    )
    parser.addoption(
        "--log_level", action="store", default="DEBUG", help="Log level"
    )


@pytest.fixture
def driver(request):
    executor = request.config.getoption("--executor")
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers_source")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    log_level = request.config.getoption("--log_level")

    if executor == 'local':
        if browser_name == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            if headless:
                chrome_options.headless = True
            _driver = webdriver.Chrome(executable_path=os.path.join(drivers_folder, 'chromedriver.exe'),
                                       options=chrome_options)
        elif browser_name == 'edge':
            _driver = webdriver.Edge(executable_path=os.path.join(drivers_folder, 'msedgedriver.exe'))
        else:
            raise ValueError(f'Browser {browser_name} is not supported.')
        _driver.base_url = base_url
        _driver.test_name = request.node.name
        _driver.log_level = log_level
    else:
        capabilities = {
            'browserName': browser_name,
            'screenResolution': '1280x720',
            'browserVersion': '107.0',
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }

        options = Options()
        _driver = webdriver.Remote(
            command_executor=executor,
            options=options,
            desired_capabilities=capabilities
        )
        _driver.base_url = base_url
        _driver.test_name = request.node.name
        _driver.log_level = log_level
    yield _driver
    _driver.close()
