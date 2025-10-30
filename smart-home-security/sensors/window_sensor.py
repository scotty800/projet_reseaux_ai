import random, time

while True:
    state = random.choice({"OPEN", "CLOSED"})
    print(f"Window is {state}")
    time.sleep(5)