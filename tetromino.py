class Tetromino:

    def __init__(self, world, pattern, color=(0, 255, 0)):
        self.world = world
        self.is_frozen = False
        self.position = [1, 1]
        self.pattern = pattern
        self.pattern_size = len(pattern)
        self.color = color  # one of the seven tetromino colors

    def rotate_counter_clockwise(self):
        self._rotate_counter_clockwise()
        if self.world.collides(self):
            self._rotate_clockwise()

    def rotate_clockwise(self):
        self._rotate_clockwise()
        if self.world.collides(self):
            self._rotate_counter_clockwise()

    def _rotate_counter_clockwise(self):
        self.pattern = list(zip(*self.pattern))[::-1]

    def _rotate_clockwise(self):
        self.pattern = list(zip(*self.pattern[::-1]))

    # advances one row down
    def advance(self):
        # if we are frozen we can't move!
        if self.is_frozen:
            return
        # check if our next coordinate is colliding
        collision = self.world.collides(self, [1, 0])
        if collision is not None:
            self.is_frozen = True
        else:
            self.position[0] += 1

    def move_left(self):
        if self.is_frozen or self.world.collides(self, [0, -1]):
            return
        self.position[1] -= 1

    def move_right(self):
        if self.is_frozen or self.world.collides(self, [0, 1]):
            return
        self.position[1] += 1

    def print(self):
        for row in self.pattern:
            print(*('#' if v else ' ' for v in row), sep='')
