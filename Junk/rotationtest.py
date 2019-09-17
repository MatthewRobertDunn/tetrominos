import tetromino
import world

print("starting")

grid = world.World(10,20)
pattern = [[0, 1, 0], [1, 1, 1], [0, 0, 0]]


piece = tetromino.Tetromino(grid,pattern)

piece.print()

piece.rotate_counter_clockwise()

piece.print()

piece.rotate_clockwise()

piece.print()


grid.draw_piece(piece)
print("world")
grid.print()

for i in range(25):
    grid.clear_piece(piece)
    piece.advance()
    grid.draw_piece(piece)
    print("world")
    grid.print()
    screen.render()
