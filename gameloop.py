import world
import renderer
import player
import controls
import pygame


def start_game():
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
