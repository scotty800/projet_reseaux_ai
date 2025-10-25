import random, time

while True:
    humidity = round(random.uniform(30, 70), 2)
    print(f"Humidité : {humidity}%")
    time.sleep(5)