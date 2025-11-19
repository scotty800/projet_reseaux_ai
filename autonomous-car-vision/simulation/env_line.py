import numpy as np
import random

class LineEnv:
    def __init__(self, width=40, height=10):
        self.width = width
        self.height = height
        self.line_pos = width // 2

    def generate_frame(self):
        frame = np.zeros((self.height, self.width))

        frame[:, self.line_pos] = 1

        move = random.choice([-1, 0, 1])
        self.line_pos += move

        # Empêcher de sortir
        self.line_pos = max(2, min(self.width - 3, self.line_pos))

        return frame
