import csv
import os

def log_detection(name, timestamp, image_filename):
    os.makedirs("logs", exist_ok=True)
    os.makedirs("logs/images", exist_ok=True)
    file_path = "logs/detections.csv"
    
    file_exists = os.path.isfile(file_path)
    
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Timestamp", "Image"])
        writer.writerow([name, timestamp, image_filename])
