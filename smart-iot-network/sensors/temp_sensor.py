import random, time

while True:
    temp = round(random.uniform(20, 30), 2)
    print(f"Température : {temp} °C")
    time.sleep(5)
