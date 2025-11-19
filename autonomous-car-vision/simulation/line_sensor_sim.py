import numpy as np

class IRSensors:
    def __init__(self, env):
        self.env = env

    def read(self):
        frame = self.env.generate_frame()

        row = frame[-1]

        mid = np.argmax(row)

        center_pos = self.env.width // 2

        left = 1 if mid < center_pos - 2 else 0

        right = 1 if mid > center_pos + 2 else 0

        center = 1 if abs(mid - center_pos) <= 2 else 0

        return left, center, right, frame
