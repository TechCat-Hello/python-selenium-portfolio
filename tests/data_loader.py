import csv
import json
import os

def load_csv_keywords():
    csv_file = os.path.join(os.path.dirname(__file__), "data", "keywords.csv")
    keywords = []
    if os.path.exists(csv_file):
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    keywords.append(row[0])
    return keywords

def load_json_keywords():
    json_file = os.path.join(os.path.dirname(__file__), "data", "keywords.json")
    keywords = []
    if os.path.exists(json_file):
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)
            keywords.extend(data)
    return keywords

def load_excel_keywords():
    try:
        import openpyxl
    except ImportError:
        raise RuntimeError("openpyxl が必要です")

    excel_file = os.path.join(os.path.dirname(__file__), "data", "keywords.xlsx")
    keywords = []
    if os.path.exists(excel_file):
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[0]:
                keywords.append(str(row[0]))
    return keywords



