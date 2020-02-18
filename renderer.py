import pygame
import tetromino
import world
import tiles

class PyGameRenderer:
    def __init__(self, game, player):
        self.screen =  pygame.display.get_surface()
        self.game = game
        self.player = player
        self.tile_size = 32
        self.grid_offset = (self.screen.get_width() / 2 - 6*self.tile_size, self.tile_size)
        self.grid_pixel_width = len(self.game.grid[0]) * self.tile_size 
        self.grid_pixel_height = len(self.game.grid) * self.tile_size 
        self.grid_surface = pygame.Surface((self.grid_pixel_width, self.grid_pixel_height))
        self.alpha = 255

    def draw(self):

        if(self.player.cleared_lines != 0):
            self.old_grid_surface = self.grid_surface
            self.grid_surface = pygame.Surface((self.grid_pixel_width, self.grid_pixel_height))
            self.alpha = 0
            print("Cleared lines!")

        self.draw_tiles(self.grid_surface)
        
        if(self.alpha == 255):
            self.screen.blit(self.grid_surface,(self.grid_offset))
        else:
            self.grid_surface.set_alpha(self.alpha)
            self.old_grid_surface.set_alpha(255 - self.alpha)
            self.screen.blit(self.old_grid_surface,(self.grid_offset))
            self.screen.blit(self.grid_surface,(self.grid_offset))
            self.alpha +=5

        self.draw_score()


    def draw_score(self):
        font = pygame.font.SysFont("monospace", 20)
        text = font.render(
            f'Super Tetrominos. Game {"Over" if self.player.game_over else "Active"}. Score: {self.player.score}'\
            , False, (255, 255, 255))
        self.screen.blit(text, (0, 0))

    def draw_tiles(self, surface):
        surface.fill((0, 0, 0))
        screenY = 0

        for row in self.game.grid:
            screenX = 0
            for cell in row:
                _draw_tile(surface,screenX, screenY, cell)
                screenX += self.tile_size
            screenY += self.tile_size

def _draw_tile(surface, screenX, screenY, cell):
    if cell is None:
        return

    if cell == 'E':
        color = tiles.BORDER_TILE
    elif cell == 'S':
        color = tiles.BORDER_TILE
    else:
        color = cell.color
    
    surface.blit(color, (screenX, screenY))
