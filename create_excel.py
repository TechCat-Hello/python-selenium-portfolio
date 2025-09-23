import pandas as pd
import os

# tests/data フォルダのパス
data_dir = os.path.join("tests", "data")
os.makedirs(data_dir, exist_ok=True)  # フォルダがなければ作成

# テスト用キーワードリスト
keywords = ["Selenium Python", "pytest tutorial", "GitHub Actions", "Selenium WebDriver"]

# 1列のみのデータフレームを作成
df = pd.DataFrame({"keyword": keywords})

# Excelファイル作成
excel_path = os.path.join(data_dir, "keywords.xlsx")
df.to_excel(excel_path, sheet_name="Sheet1", index=False)

print(f"Excelファイル '{excel_path}' を作成しました。")

