import time
from sensor_sim import read_temp
from mqtt_client import publish_temp

try:
    while True:
        temp = read_temp()
        publish_temp(temp)
        print("Sent:", temp)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopped by user")