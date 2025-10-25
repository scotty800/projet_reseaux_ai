import random, time

while True:
    light = round(random.uniform(0, 1000))
    print(f"Luminosité : {light} lux")
    time.sleep(5)