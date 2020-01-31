import menu_player
import pygame

class MenuRenderer:
    def __init__(self, player):
        self.player = player
        self.screen = pygame.display.get_surface()
        self.font =  pygame.font.SysFont("monospace", 20)

    def draw_menu(self):
        height = 20
        for item in self.player.menu_items:
            text = self.render_text(item.Text, item.Selected)
            self.screen.blit(text, (0, height))
            height += 10


    def render_text(self, text, selected):
        color = (127, 127, 127)
        if selected:
            color = (255, 255, 255)
        return self.font.render(text, True, color)
