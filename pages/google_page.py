from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage:
    URL = "https://www.google.com"
    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load(self):
        """Open Google top page."""
        self.driver.get(self.URL)

    def search(self, text):
        """Enter text into search box and submit."""
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_box.clear()
        search_box.send_keys(text)
        search_box.submit()

    def title_contains(self, text, timeout=10):
        """Return True when title contains text (waits up to timeout)."""
        return WebDriverWait(self.driver, timeout).until(EC.title_contains(text))
