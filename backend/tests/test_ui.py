import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    # 1. Configure Chrome to run headlessly inside Docker
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # 2. Point to the selenium container service defined in docker-compose
    selenium_url = "http://selenium-chrome:4444/wd/hub"
    
    driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_google_title(driver):
    # Test checking if a basic page resolves
    driver.get("https://www.google.com")
    assert "Google" in driver.title