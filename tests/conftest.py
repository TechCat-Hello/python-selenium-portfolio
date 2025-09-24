import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Provides a webdriver.Chrome instance for testing.
    - Headless mode is automatically enabled in CI (GitHub Actions)
    - Local environment can override with HEADLESS=1
    """
    options = webdriver.ChromeOptions()

    # CI環境（GitHub Actions）なら自動でヘッドレス
    if os.environ.get("GITHUB_ACTIONS") == "true" or os.environ.get("HEADLESS", "0") == "1":
        options.add_argument("--headless")  # 画面表示なし
        options.add_argument("--no-sandbox")  # CI用
        options.add_argument("--disable-dev-shm-usage")  # CI用
        options.add_argument("--window-size=1920,1080")  # 必要に応じてウィンドウサイズ指定

    else:
        # ローカルではブラウザを最大化
        options.add_argument("--start-maximized")

    # ChromeDriver を自動管理
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        yield driver
    finally:
        driver.quit()

