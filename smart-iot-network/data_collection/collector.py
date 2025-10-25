import csv, random, time
import os

os.makedirs("data", exist_ok=True)

with open("data/sensor_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "temperature", "humidity", "light"])

    while True:
        temp = round(random.uniform(20, 30), 2)
        humidity = round(random.uniform(30, 70), 2)
        light = round(random.uniform(0, 1000))
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        writer.writerow([timestamp, temp, humidity, light])

        print(f"{timestamp} | Temp: {temp} °C | Humidity: {humidity}% | Light: {light} lux")
        time.sleep(5)