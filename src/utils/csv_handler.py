import csv
from pathlib import Path

import models
import config



# Change the CSV path in the configuration.
def set_csv_file_dir(csv_file_name:str):
    csv_dir = config.BASE_DIR / "data" / f"{csv_file_name}.csv"
    config.CSV_FILE_DIR = csv_dir



# Transfrom the CSV file to the objects, then put them into a list.
def csv_to_list(csv_dir:Path):
    object_list = []

    with open(csv_dir, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)  # 用表头作为 key
        for row in reader:
            # Trsfrom the data to the tuple, then put it into the list.
            term = row['Term']
            subject = row['Subject']
            credit = float(row['Credit'])
            grade = float(row['Grade'])

            new_grade_record = models.GradeRecord(term, subject, credit, grade)

            object_list.append(new_grade_record)
    
    return object_list


# Load CSV File.
def load_csv():
    config.CURRENT_STATUS = "[Load CSV File]"

    csv_file_name = input(f"{config.CURRENT_STATUS} CSV file name: ")

    try:
        set_csv_file_dir(csv_file_name)
        config.CURRENT_OBJECT_LIST = csv_to_list(config.CSV_FILE_DIR)
        print(f"{config.CURRENT_STATUS} CSV file loaded successfully!")

        config.CURRENT_STATUS = f"[{csv_file_name}]"
        config.CURRENT_CSV_FILE_NAME = csv_file_name   
    except:
        print(f"[Error] Something wrong. Please input the correct CSV file name.")
        config.CSV_FILE_DIR = None
        config.CURRENT_STATUS = None


# Check if user has loaded a CSV.
def csv_load_checker():
    if not config.CSV_FILE_DIR:
        raise RuntimeError("You haven't loaded the CSV file yet!")