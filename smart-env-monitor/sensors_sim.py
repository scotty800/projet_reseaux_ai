import random

def get_temp():
    return round(random.uniform(15, 40), 1)

def get_humidity():
    return round(random.uniform(20, 90), 1)

def get_light():
    return round(random.uniform(100, 1000), 1)

if __name__ == "__main__":
    print("Temperature:", get_temp(), "°C")
    print("Humidity:", get_humidity(), "%")
    print("Light Level:", get_light(), "lux")