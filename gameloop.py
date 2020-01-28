import world
import renderer
import player
import controls
import pygame
import tetris_screen

def start_game():
    screen = tetris_screen.TetrisScreen()
    start_screen(screen)

def start_game_old():
    print("starting")
    game = world.World(10, 20)
    keys = controls.Controls()
    p1 = player.Player(game, keys)
    screen = renderer.PyGameRenderer(game, p1, 800, 600)
    clock = pygame.time.Clock()
    old_keys = keys.snapshot()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        ticks = clock.tick(60)
        p1.tick(ticks, keys, old_keys)
        old_keys = keys.snapshot()
        screen.draw_tiles()
        screen.draw_score()
        pygame.display.flip()



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
