import tetromino
import tetrominos
import random

class Player:

    def __init__(self, game, controls):
        self.game = game
        self.controls = controls
        self.game_over = False
        self.tetromino = None
        self.score = 0
        self.repeat_delay = 250
        self.move_left_held = 0
        self.move_right_held = 0
        self.advance_held = 0

    def tick(self, ticks, controls, old_controls):
        if self.game_over:
            return
        tetromino = self._get_tetromino()

        self.game.clear_piece(tetromino)

        if controls.advance:
            if self.advance_held == 0 or self.advance_held > self.repeat_delay:
                tetromino.advance()
            self.advance_held += ticks
        else:
            self.advance_held = 0

        if controls.move_left:
            if self.move_left_held == 0 or self.move_left_held > self.repeat_delay:
                tetromino.move_left()
            self.move_left_held += ticks
        else:
            self.move_left_held = 0

        if controls.move_right:
            if self.move_right_held == 0 or self.move_right_held > self.repeat_delay:
                tetromino.move_right()
            self.move_right_held += ticks
        else:
            self.move_right_held = 0

        if not old_controls.rotate_clockwise and controls.rotate_clockwise:
            tetromino.rotate_clockwise()

        self.game.place_piece(tetromino)

        if tetromino.is_frozen:
            cleared_lines = self.game.clear_lines()
            self.score += 2**cleared_lines

    # Returns the tetromino under control by the player
    def _get_tetromino(self):
        if self.tetromino is None or self.tetromino.is_frozen:
            self.tetromino = self._get_new_tetromino()
            if self.game.collides(self.tetromino):
                self.game_over = True

        return self.tetromino

    # spawns a new piece into the world
    def _get_new_tetromino(self):
        pattern = random.choice(tetrominos.all_patterns)
        return tetromino.Tetromino(self.game, *pattern)
