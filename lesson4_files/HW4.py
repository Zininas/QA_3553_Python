
def save_shopping_list(items):
    with open("shopping.txt", "w", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")

items = [
    "Milk",
    "Bread",
    "Apples",
    "Coffee"
]

save_shopping_list(items)

import csv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "students.csv")

csv_content = """name,age
Anna,21
Tom,19
Kate,22"""

with open(csv_path, "w", encoding="utf-8", newline="") as file:
    file.write(csv_content)

def read_students(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student: {row['name']} ({row['age']})")

read_students(csv_path)

import json
import os

def save_profile(name, age, city):
    profile_dict = {
        "name": name,
        "age": age,
        "city": city
    }

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "profile.json")

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(profile_dict, file, indent=4, ensure_ascii=False)

save_profile("Maria", 30, "Haifa")

from pathlib import Path

def create_reports_folder():
    current_dir = Path(__file__).resolve().parent
    reports_dir = current_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    file_path = reports_dir / "result.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Homework completed successfully!\n")

    print(f"Папка и файл успешно созданы по пути: {file_path}")

create_reports_folder()