import random

def get_temp():
    return round(random.uniform(15.0, 25.0), 1)

def get_humidity():
    return round(random.uniform(20.0, 80.0), 1)

def get_light():
    return round(random.uniform(0, 1023))

if __name__ == "__main__":
    print("Temperature:", get_temp(), "°C")
    print("Humidity:", get_humidity(), "%")
    print("Light Level:", get_light())