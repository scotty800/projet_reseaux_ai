import time, csv, os
from sensors_sim import get_temp, get_humidity, get_light
from logic_ai import decide

LOG_FILE = "data_log.csv"

def log(temp, hum, light):
    exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline= '') as f:
        writer = csv.writer(f)
        time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        if not exists:
            writer.writerow(["Timestamp", "Temperature", "Humidity", "Light"])
        writer.writerow([time_stamp, temp, hum, light])

while True:
    t = get_temp()
    h = get_humidity()
    l = get_light()
    decide(t, h, l)
    log(t, h, l)
    print(t, h, l)
    time.sleep(2)