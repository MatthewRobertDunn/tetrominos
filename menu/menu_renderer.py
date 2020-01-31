import menu_player
import pygame

class MenuRenderer:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen

    def draw_menu(self):
        font = pygame.font.SysFont("monospace", 20)
        text = font.render(
            f'Super Tetrominos. Game {"Over" if self.player.game_over else "Active"}. Score: {self.player.score}'\
            , True, (255, 255, 255))
        self.screen.blit(text, (0, 0))
