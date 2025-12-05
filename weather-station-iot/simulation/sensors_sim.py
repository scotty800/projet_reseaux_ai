import random

def get_temp():
    return round(random.uniform(10.0, 40.0), 1)

def get_humidity():
    return round(random.uniform(10.0, 90.0), 1)

def get_pressure():
    return round(random.uniform(950.0, 1050.0), 1)

def get_light():
    return random.randint(0, 1023)

if __name__ == "__main__":
    print("Temperature:", get_temp(), "°C")
    print("Humidity:", get_humidity(), "%")
    print("Pressure:", get_pressure(), "hPa")
    print("Light Level:", get_light()) 