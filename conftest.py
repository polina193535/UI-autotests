import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    Pytest fixture for initializing and quitting Chrome WebDriver.
    Запускает браузер Chrome перед тестом и закрывает после теста.
    """
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    yield driver
    try:
        driver.quit()
    except Exception as e:
        print(f"Error during driver.quit(): {e}")
