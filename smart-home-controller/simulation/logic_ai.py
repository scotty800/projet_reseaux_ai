fom actuators_sim import turn_on, turn_off

def decide(temp, hum, light):
    if temp > 28: turn_on("Fan"); turn_off("Heater")
    elif temp < 20: turn_on("Heater"); turn_off("Fan")
    else: turn_off("Fan"); turn_off("Heater")

    if light < 300: turn_on("Lamp")
    elif light > 700: turn_off("Lamp")