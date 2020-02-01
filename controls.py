import pygame
import types

# keeps state of the game controls
# primarily to abstract game logic from pygame
class Controls:
    def __init__(self):
        pygame.init()

    def read(self):
        c = types.SimpleNamespace()
        keys = pygame.key.get_pressed()
        c.advance = self.advance(keys)
        c.rotate_clockwise = self.rotate_clockwise(keys)
        c.rotate_counter_clockwise = self.rotate_counter_clockwise(keys)
        c.move_left = self.move_left(keys)
        c.move_right = self.move_right(keys)
        c.menu_up = self.menu_up(keys)
        c.menu_down = self.menu_down(keys)
        c.menu_select = self.menu_select(keys)
        return c

    
    def advance(self ,keys):
        return keys[pygame.K_SPACE]

    def rotate_clockwise(self,keys):
        return keys[pygame.K_DOWN]

    def rotate_counter_clockwise(self, keys):
        return keys[pygame.K_UP]

    def move_left(self, keys):
        return keys[pygame.K_LEFT]

    def move_right(self, keys):
        return keys[pygame.K_RIGHT]

    def menu_up(self, keys):
        return keys[pygame.K_UP]

    def menu_down(self, keys):
        return keys[pygame.K_DOWN]
    
    def menu_select(self, keys):
        return keys[pygame.K_RETURN]
