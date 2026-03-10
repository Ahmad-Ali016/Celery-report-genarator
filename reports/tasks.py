import csv
import os
import random
from datetime import datetime

from celery import shared_task
import time
from django.conf import settings
from faker import Faker


@shared_task
def add(x, y):
    # Simple test task that adds two numbers.
    # time.sleep(5)  # simulate a time-consuming task
    return x + y

@shared_task
def generate_csv():

    # Generates a dummy CSV with sample data and saves it to a folder. Returns the file path.

    # Folder to save CSV
    folder = os.path.join(settings.BASE_DIR, "generated_csvs")
    os.makedirs(folder, exist_ok=True)

    # CSV file path
    file_path = os.path.join(folder, "sample.csv")

    # Dummy data
    data = [
        ["ID", "Name", "Score"],
        [1, "Alice", 95],
        [2, "Bob", 88],
        [3, "Charlie", 76],
    ]

    # Write CSV
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    return file_path


fake = Faker()

@shared_task
def generate_csv_task(num_rows=5):
    folder = 'generated_csvs'
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'report_{timestamp}.csv'
    file_path = os.path.join(folder, filename)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Name', 'Score'])
        for i in range(1, num_rows + 1):
            writer.writerow([i, fake.name(), random.randint(0, 100)])

    return file_path