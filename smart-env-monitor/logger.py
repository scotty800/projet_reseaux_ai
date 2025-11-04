import csv, time, os

LOG_FILE = "data/logs.csv"

def log_data(temp, hum, light, status):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        if not file_exists:
            writer.writerow(["Timestamp", "Temperature", "Humidity", "Light", "Status"])
        writer.writerow([timestamp, temp, hum, light, status])