import constants
import os
import pygame

    

def _load(x):
    tile =  pygame.image.load(os.path.join(constants.TILES_DIR, x ))
    return pygame.transform.scale(tile,(32,32))

RED_TILE = _load("RedBlockFX.png")
BLUE_TILE = _load("BlueBlockFX.png")
YELLOW_TILE = _load("YellowBlockFX.png")
GREEN_TILE = _load("GreenBlockFX.png")
GRAY_TILE = _load("GrayBlockFX.png")
ORANGE_TILE = _load("OrangeBlockFX.png")
PINK_TILE = _load("PinkBlockFX.png")
BORDER_TILE = _load("GrayBlockShatteringFX.png")
