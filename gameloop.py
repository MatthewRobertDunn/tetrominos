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
    pygame.display.set_mode((1024, 768))
    menu_screen = menu.main_screen.MainScreen()
    start_screen(menu_screen)



def start_new_game():
     _change_screen(tetris_screen.TetrisScreen())


_next_screen = None
def _change_screen(screen):
    global _next_screen 
    _next_screen = screen

def quit():
    pygame.quit()
    sys.exit()

def start_screen(screen):
    global _next_screen 
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
        if _next_screen is not None:
            screen = _next_screen
            _next_screen = None
            pygame.display.get_surface().fill((0,0,0))
        keys = key_reader.read()
        screen.tick(ticks, keys, old_keys)
        old_keys = keys
        screen.draw()
        pygame.display.flip()
