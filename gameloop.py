import world
import renderer
import player
import controls
import pygame
import tetris_screen
import menu.main_screen
import sys

def start_game():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init() #don't change the order of these or odd sound issues happen
    pygame.mixer.set_num_channels(8)
    pygame.init()
    pygame.display.set_mode((800, 600))
    screen = tetris_screen.TetrisScreen()
    menu_screen = menu.main_screen.MainScreen()
    start_screen(menu_screen)


def start_screen(screen):
    print("starting")
    clock = pygame.time.Clock()
    key_reader = controls.Controls()
    old_keys = key_reader.read()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                pygame.quit()
                sys.exit()
                break
        ticks = clock.tick(60)
        keys = key_reader.read()
        screen.tick(ticks, keys, old_keys)
        old_keys = keys
        screen.draw()
        pygame.display.flip()
