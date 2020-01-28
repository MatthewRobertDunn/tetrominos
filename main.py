import tetromino
import world
import renderer
import time
import gameloop
import pygame
import numpy as np

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font(None, 20)

gameloop.start_game()
