import random

def read_temp():
    return round(random.uniform(20, 50), 2)

if __name__ == "__main__":
    print(read_temp())