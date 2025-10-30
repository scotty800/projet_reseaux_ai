import random, time

while True:
    state = random.choice(['MOTION', 'NO MOTION'])
    print(f"Motion sensor is {state}")
    time.sleep(5)