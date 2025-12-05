import time, csv, os
from sensor_sim import get_humidity, get_light, get_pressure, get_temp
from alerts_ai import dectect_events

LOG_FILE = "data/log.csv"

def log(temp, hum, press, light, events):
    exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if not exists:
            writer.writerow(["Timestamp", "Temperature", "Humidity", "Pressure", "Light", "Events"])
        writer.writerow([timestamp, temp, hum, press, light, ";".join(events)])

while True:
    temp = get_temp()
    hum = get_humidity()
    press = get_pressure()
    light = get_light()
    events = dectect_events(temp, hum, press, light)

    print(temp, hum, press, light, events)

    log(temp, hum, press, light, events)

    time.sleep(2)