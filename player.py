import tetromino
import tetrominos
import random
import math

class Player:

    def __init__(self, game, controls):
        self.game = game
        self.controls = controls
        self.game_over = False
        self.tetromino = None
        self.score = 0

    def tick(self):
        if self.game_over:
            return
        tetromino = self._get_tetromino()

        self.game.clear_piece(tetromino)

        if self.controls.advance:
            tetromino.advance()

        if self.controls.move_left:
            tetromino.move_left()

        if self.controls.move_right:
            tetromino.move_right()

        if self.controls.rotate_clockwise:
            tetromino.rotate_clockwise()

        self.game.place_piece(tetromino)

        if tetromino.is_frozen:
            cleared_lines = self.game.clear_lines()
            self.score += 2**cleared_lines

    # Returns the tetromino under control by the player
    def _get_tetromino(self):
        if self.tetromino is None or self.tetromino.is_frozen:
            self.tetromino = self._get_new_tetromino()

        return self.tetromino

    # spawns a new piece into the world
    def _get_new_tetromino(self):
        pattern = random.choice(tetrominos.all_patterns)
        return tetromino.Tetromino(self.game, *pattern)

