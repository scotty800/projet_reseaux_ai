def dectect_events(temp, hum, press, light):
    event = []
    
    if temp > 35.0:
        event.append("wave_heat")
    elif temp < 15.0:
        event.append("cold_alert")
    if press < 990.0:
        event.append("storm_risk")
    if hum > 80.0:
        event.append("rain_risk")
    if light < 200:
        event.append("night_mode")

    return event

if __name__ == "__main__":
    print(dectect_events(36.5, 85.0, 985.0, 150))  # Example usage