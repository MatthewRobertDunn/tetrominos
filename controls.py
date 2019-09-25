import pygame
import types

# keeps state of the game controls
# primarily to abstract game logic from pygame
class Controls:
    def __init__(self):
        pygame.init()

    def snapshot(self):
        c = types.SimpleNamespace()
        c.advance = self.advance
        c.rotate_clockwise = self.rotate_clockwise
        c.rotate_counter_clockwise = self.rotate_counter_clockwise
        c.move_left = self.move_left
        c.move_right = self.move_right
        return c

    @property
    def advance(self):
        keys = pygame.key.get_pressed()
        return keys[pygame.K_SPACE]

    @property
    def rotate_clockwise(self):
        keys = pygame.key.get_pressed()
        return keys[pygame.K_DOWN]

    @property
    def rotate_counter_clockwise(self):
        keys = pygame.key.get_pressed()
        return keys[pygame.K_UP]

    @property
    def move_left(self):
        keys = pygame.key.get_pressed()
        return keys[pygame.K_LEFT]

    @property
    def move_right(self):
        keys = pygame.key.get_pressed()
        return keys[pygame.K_RIGHT]
