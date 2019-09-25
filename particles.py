import numpy as np


class Confetti:
    def __init__(self, width, height, count):
        self.width = width,
        self.height = height,
        self.count = count
        # prepare our positions matrix
        positions = np.matrix(np.random.rand(2, count))
        # scale our particles into the requested area
        scale = np.matrix([[width, 0], [0, height]])
        self.positions = scale * positions
