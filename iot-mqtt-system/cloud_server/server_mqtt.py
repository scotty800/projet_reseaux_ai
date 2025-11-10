import paho.mqtt.client as mqtt
import csv, time, os

LOG = "data/temps.csv"
os.makedirs("data", exist_ok=True)

def write_temp(temp):
    file_exists = os.path.isfile(LOG)
    with open(LOG, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["time", "temp"])
        writer.writerow([time.strftime("%H:%M:%S"), temp])

def on_message(client, userdata, msg):
    temp = float(msg.payload.decode())
    write_temp(temp)
    print("Received:", temp)

client = mqtt.Client()
client.connect("localhost", 1883)

client.subscribe("iot/temp")
client.on_message = on_message

print("Listening for temperature data...")
client.loop_forever()
