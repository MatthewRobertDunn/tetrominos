import pygame
import tetromino
import world


class PyGameRenderer:
    def __init__(self, game, player):
        self.screen =  pygame.display.get_surface()
        self.game = game
        self.player = player
        self.tile_size = 16
        self.grid_offset = [self.screen.get_width() / 2 - 100, 128]

    def draw_score(self):
        font = pygame.font.SysFont("monospace", 20)
        text = font.render(
            f'Super Tetrominos. Game {"Over" if self.player.game_over else "Active"}. Score: {self.player.score}'\
            , True, (255, 255, 255))
        self.screen.blit(text, (0, 0))

    def draw_tiles(self):
        self.screen.fill((0, 0, 0))
        screenY = self.grid_offset[1]

        for row in self.game.grid:
            screenX = self.grid_offset[0]
            for cell in row:
                self._draw_tile(screenX, screenY, cell)
                screenX += self.tile_size + 1
            screenY += self.tile_size + 1

    def _draw_tile(self, screenX, screenY, cell):
        if cell is None:
            return

        if cell == 'E':
            color = (255, 0, 0)
        elif cell == 'S':
            color = (0, 0, 255)
        else:
            color = cell.color
        pygame.draw.rect(self.screen, color, (screenX, screenY, self.tile_size, self.tile_size), 3)
