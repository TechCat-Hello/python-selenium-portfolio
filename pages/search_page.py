from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        
    def load(self):
        # demo_pages/search.html の絶対パスを取得
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../demo_pages/search.html"))
        # Windows の場合に / に置換して file:// で開く
        file_url = "file:///" + file_path.replace("\\", "/")
        self.driver.get(file_url)

    
    def search(self, keyword):
        wait = WebDriverWait(self.driver, 10)
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-box"))
        )
        search_box.clear()
        search_box.send_keys(keyword)
        search_button = self.driver.find_element(By.ID, "search-button")
        search_button.click()
    
        # 検索結果がロードされるのを待つ（div#resultsが表示される想定）
        wait.until(EC.presence_of_element_located((By.ID, "results")))
    
    def results_contain(self, keyword):
        results = self.driver.find_element(By.ID, "results")
        return keyword in results.text
