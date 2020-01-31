import world
import renderer
import player
import controls
import pygame
import tetris_screen
import menu.main_screen

def start_game():
    pygame.init()
    pygame.display.set_mode((800, 600))
    screen = tetris_screen.TetrisScreen()
    menu = menu.main_screen.MainScreen()
    start_screen(menu)


def start_screen(screen):
    print("starting")
    clock = pygame.time.Clock()
    key_reader = controls.Controls()
    old_keys = key_reader.read()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        ticks = clock.tick(60)
        keys = key_reader.read()
        screen.tick(ticks, keys, old_keys)
        old_keys = keys
        screen.draw()
        pygame.display.flip()
