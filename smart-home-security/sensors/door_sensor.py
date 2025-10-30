import random, time

while True:
    state = random.choice(['OPEN', "CLOSED"])
    print(f"Door is {state}")
    time.sleep(5)