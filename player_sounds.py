import constants
import pygame
import os

class PlayerSounds:
    def __init__(self):
        self.freeze_sample = pygame.mixer.Sound(os.path.join(constants.SOUND_DIR, 'freeze.ogg'))
        

    def freeze(self):
        chan = pygame.mixer.find_channel(True)
        chan.queue(self.freeze_sample)
