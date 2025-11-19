from env_line import LineEnv
from sensors_line import IRSensors
from pid import PID
import time

env = LineEnv()
sensor = IRSensors(env)
pid = PID(kp=0.4, ki=0.0, kd=0.2)

while True:
    left, center, right, frame = sensor.read()

    error = (right - left)

    correction = pid.compute(error)

    if correction > 0.5:
        action = "RIGHT"
    elif correction < -0.5:
        action = "LEFT"
    else:
        action = "FORWARD"

    print("ACTION:", action, " | PID:", round(correction,2))

    time.sleep(0.2)
