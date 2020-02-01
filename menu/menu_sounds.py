import constants
import pygame
import os

class MenuSounds:
    def __init__(self):
        self.menu_select_sample = pygame.mixer.Sound(os.path.join(constants.SOUND_DIR, 'menu_select.ogg'))
        pygame.mixer.music.load(os.path.join(constants.MUSIC_DIR, 'tetrominos.ogg'))

    def menu_select(self):
        chan = pygame.mixer.find_channel(True)
        chan.queue(self.menu_select_sample)
        

    def menu_music(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
