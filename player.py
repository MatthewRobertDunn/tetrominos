import tetromino
import tetrominos
import random
import player_sounds
class Player:

    def __init__(self, game):
        self.game = game
        self.game_over = False
        self.tetromino = None
        self.score = 0
        self.repeat_delay = 250
        self.move_left_held = 0
        self.move_right_held = 0
        self.advance_held = 0
        self.move_speed = 60
        self.last_move = 0
        self.cleared_lines = 0
        self.sounds = player_sounds.PlayerSounds()

    def tick(self, ticks, controls, old_controls):
        if self.game_over:
            return
        tetromino = self._get_tetromino()

        self.game.clear_piece(tetromino)

        if controls.advance:
            if self.advance_held == 0:
                tetromino.advance()
            self.advance_held += ticks
            self._move_piece(self.advance_held,ticks,tetromino.advance)
        else:
            self.advance_held = 0

        if controls.move_left:
            if self.move_left_held == 0:
                tetromino.move_left()
            self.move_left_held += ticks
            self._move_piece(self.move_left_held,ticks,tetromino.move_left)
        else:
            self.move_left_held = 0

        if controls.move_right:
            if self.move_right_held == 0:
                tetromino.move_right()
            self.move_right_held += ticks
            self._move_piece(self.move_right_held,ticks,tetromino.move_right)
        else:
            self.move_right_held = 0

        if not old_controls.rotate_clockwise and controls.rotate_clockwise:
            tetromino.rotate_clockwise()

        self.game.place_piece(tetromino)
        self.cleared_lines = 0
        if tetromino.is_frozen:
            self.cleared_lines =  self.game.clear_lines()
            self.score += 2**self.cleared_lines
            self.sounds.freeze()

    # Returns the tetromino under control by the player
    def _get_tetromino(self):
        if self.tetromino is None or self.tetromino.is_frozen:
            self.tetromino = self._get_new_tetromino()
            if self.game.collides(self.tetromino):
                self.game_over = True

        return self.tetromino

    # moves a piece while limiting max speed
    def _move_piece(self, held, ticks, move_func):
        if held > self.repeat_delay and self.last_move > self.move_speed:
            move_func()
            self.last_move = 0
        else:
            self.last_move += ticks

    # spawns a new piece into the world
    def _get_new_tetromino(self):
        pattern = random.choice(tetrominos.all_patterns)
        return tetromino.Tetromino(self.game, *pattern)
