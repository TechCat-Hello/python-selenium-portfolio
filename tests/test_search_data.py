import sys
import os
import pytest
from pages.search_page import SearchPage
from tests.data_loader import load_csv_keywords, load_json_keywords, load_excel_keywords
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # GUI表示させたい場合は headless コメントアウト
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

# CSV/JSON/Excelのキーワードをまとめて取得
keywords = []
keywords += load_csv_keywords()
keywords += load_json_keywords()
try:
    keywords += load_excel_keywords()
except RuntimeError:
    pass

if not keywords:
    pytest.skip("No keywords found in tests/data/", allow_module_level=True)

@pytest.mark.data_driven
@pytest.mark.parametrize("keyword", keywords)
def test_search_data(driver, keyword):
    page = SearchPage(driver)
    page.load()
    page.search(keyword)
    assert page.results_contain(keyword)

    # スクリーンショット保存用ディレクトリを作成
    screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    # 保存ファイルパスを作成
    file_path = os.path.join(screenshot_dir, f"screenshot_search_{keyword}.png")
    driver.save_screenshot(file_path)

