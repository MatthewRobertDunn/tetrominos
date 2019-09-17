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

    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        p1.tick()
        screen.draw_tiles()
        screen.draw_score()
        pygame.display.flip()
