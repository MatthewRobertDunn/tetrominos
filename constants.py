import os
import pathlib
HOME_DIR = pathlib.Path(__file__).parent.absolute()

RESOURCE_DIR = "res"
IMAGE_DIR = os.path.join(HOME_DIR, RESOURCE_DIR, "images")
FONT_DIR = os.path.join(HOME_DIR, RESOURCE_DIR, "fonts")
SOUND_DIR = os.path.join(HOME_DIR, RESOURCE_DIR, "sounds")
MUSIC_DIR = os.path.join(HOME_DIR, RESOURCE_DIR, "music")
