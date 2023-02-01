import pytest
#import os
import yaml

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def config():
    with open('config.yml', 'r') as f:
        return yaml.safe_load(f)

@pytest.fixture()
def driver(config):
    options = Options()
    # options.add_argument("start-maximized"); # open Browser in maximized mode
    # options.add_argument("disable-infobars"); # disabling infobars
    # options.add_argument("--disable-extensions"); # disabling extensions
    # options.add_argument("--disable-gpu"); # applicable to windows os only
    # options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
    options.add_argument("--no-sandbox")
    options.add_argument("headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()