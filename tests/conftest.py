import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Provides a webdriver.Chrome instance.
    Set environment variable HEADLESS=1 to run in headless mode:
    PowerShell: $env:HEADLESS="1"; pytest ...
    """
    options = webdriver.ChromeOptions()
    # Headless is off by default to allow visual debugging.
    if os.environ.get("HEADLESS", "0") == "1":
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    try:
        yield driver
    finally:
        driver.quit()

