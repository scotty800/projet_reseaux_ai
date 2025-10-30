import csv, random, time
import os

os.makedirs("data", exist_ok=True)

with open("data/sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "door", "window", "motion"])

    while True:
        door = random.choice(['OPEN', 'CLOSED'])
        window = random.choice(['OPEN', 'CLOSED'])
        motion = random.choice(['MOTION', 'NO MOTION'])
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        writer.writerow([timestamp, door, window, motion])
        file.flush()

        print(f"Time: {timestamp} | Door: {door} | Window: {window} | Motion: {motion}")
        time.sleep(5)
