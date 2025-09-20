import pytest
import sys
import os
from pages.google_page import GooglePage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.mark.google_search
def test_google_search_pom(driver):
    """
    POM-based test:
    - load Google
    - search "Selenium Python"
    - assert title contains "Selenium"
    """
    page = GooglePage(driver)
    page.load()
    page.search("Selenium Python")
    assert page.title_contains("Selenium")
