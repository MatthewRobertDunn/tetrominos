import constants
import pygame
import os
from . import menu_player


class MenuRenderer:
    def __init__(self, player):
        self.player = player
        self.screen = pygame.display.get_surface()
        self.font =  pygame.font.Font(os.path.join(constants.FONT_DIR, 'kremlin.ttf'),70)
        self.background = pygame.image.load(os.path.join(constants.BACKGROUNDS_DIR, 'background.png'))

    def draw_menu(self):
        self.screen.blit(self.background, (0,30))
        text = self.render_text(self.player.text, True)
        self.screen.blit(text, (50, 0))

        height = 100
        for item in self.player.menu_items:
            text = self.render_text(item.text, item.selected)
            self.screen.blit(text, (50, height))
            height += self.screen.get_height() / 10.0

    def render_text(self, text, selected):
        color = (127, 127, 127)
        if selected:
            color = (255, 255, 255)
        return self.font.render(text, False, color)
