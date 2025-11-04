import time 
from sensor_sim import get_humidity, get_light, get_temp
from logger import log_data
from logic import check_temp

while True:
    temperature = get_temp()
    humidity = get_humidity()
    light = get_light()

    status = check_temp(temperature)

    print(f"Temp: {temperature} °C, Humidity: {humidity} %, Light: {light} lux, Status: {status}")
    log_data(temperature, humidity, light, status)

    time.sleep(2)