import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Provides a webdriver.Chrome instance for testing.
    - Headless is OFF by default (so you can see the browser)
    - Use HEADLESS=1 environment variable to run headless if needed
    """
    options = webdriver.ChromeOptions()

    # ヘッドレスにしたい場合のみ有効
    if os.environ.get("HEADLESS", "0") == "1":
        options.add_argument("--headless")

    # Windows環境では必須ではないオプションは削除
    # Linux向けオプションはコメントアウト
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    # ブラウザ表示を最大化
    options.add_argument("--start-maximized")

    # ChromeDriver を自動管理
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        yield driver
    finally:
        driver.quit()

