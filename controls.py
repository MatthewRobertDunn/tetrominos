import pygame


# keeps state of the game controls
# primarily to abstract game logic from pygame
class Controls:
    def __init__(self):
        pygame.init()

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

