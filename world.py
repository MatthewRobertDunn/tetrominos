import tetromino
import math


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # flattened world grid
        self._max_width = width + 2  # room for the border
        self._max_height = height + 2
        self.grid = [[None]*self._max_width for j in range(self._max_height)]

        # Put a border on the top and bottom
        for y in range(0, self._max_height):
            self.grid[y][0] = "S"  # e for edge?
            self.grid[y][-1] = "S"

        self.grid[0] = ['E']*self._max_width
        self.grid[-1] = ['E']*self._max_width

    # draws a piece onto the world
    def place_piece(self, piece):
        self._render_piece(piece)

    # clears a piece from the world
    def clear_piece(self, piece):
        self._render_piece(piece, True)

    # returns true if a piece collides with any other piece in the world other than itself
    def collides(self, piece, offset=None):
        coord = piece.position
        if offset:
            coord = coord[0] + offset[0], coord[1] + offset[1]
        for x in range(piece.pattern_size):
            for y in range(piece.pattern_size):
                if(piece.pattern[x][y] == 1):
                    cell = self.grid[coord[0] + x][coord[1] + y]
                    if cell is not None and cell != piece:
                        return cell
        return None

    # draws a single piece onto the world grid
    def _render_piece(self, piece, clear=False):
        coord = piece.position
        for x in range(piece.pattern_size):
            for y in range(piece.pattern_size):
                if(piece.pattern[x][y] == 1):
                    if clear:
                        self.grid[coord[0] + x][coord[1] + y] = None
                    else:
                        self.grid[coord[0] + x][coord[1] + y] = piece

    # returns a fresh row list
    def fresh_row(self):
        row = [None]*self._max_width
        row[0] = row[-1] = 'S'
        return row
    
    # clears out full rows, constructing a new grid by moving
    # the old rows into new grid, skipping filled rows.
    # counts how many were skipped not counting top and bottom
    # then assembles new grid by adding top, that many fresh rows
    # then the non filled rows from before, then the bottom
    # returns count of cleared lines
    def clear_lines(self):
        saved_rows = [row for row in self.grid if not all(row)]
        cleared = self.height - len(saved_rows)
        new_rows = [self.fresh_row() for c in range(cleared)]
        newgrid = [self.grid[0]] + new_rows + saved_rows + [self.grid[-1]]
        self.grid = newgrid
        return cleared

    def print(self):
        for row in self.grid:
            print(*('#' if v else ' ' for v in row), sep='')
