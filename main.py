import tetromino
import world
import renderer
import time
import gameloop
import pygame
pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font(None, 20)

gameloop.start_game()

print("starting")
game = world.World(10, 20)

screen = renderer.PyGameRenderer(game, 800, 600)

row_test_piece = [0]*10
for i in range(10):
    row_test_piece[i] = [i & 1] * 10
    if not i & 1:
        row_test_piece[i][5] = 1

piece = tetromino.Tetromino(game, row_test_piece)
game.place_piece(piece)
game.print()
print('\n')
game.clear_lines()
game.print()

screen.draw_tiles()
time.sleep(20)
