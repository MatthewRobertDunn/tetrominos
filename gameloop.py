import world
import renderer
import player
import controls
import pygame
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d import core

import tetris_screen
import menu.main_screen
import sys

class MyApp(ShowBase):
    def __init__(self):
        super()
        self.setBackgroundColor(0, 0, 0)
        lens = core.OrthographicLens()
        lens.setFilmSize(80*0.8, 60*0.8)  # Or whatever is appropriate for your scene
        self.cam.node().setLens(lens)
        self.cam.setPos(9,0,19)
        self.taskMgr.add(self.game_tick, "game_tick")
        self._key_reader = controls.Controls()
        self._old_keys = self._key_reader.read()

    def change_screen(self, screen):
        self._next_screen = screen

    def game_tick(self, task):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                pygame.quit()
                sys.exit()
                break
        
        if self._next_screen is not None:
            self._screen = self._next_screen
            self._next_screen = None

        keys = self._key_reader.read()
        self._screen.tick(task.time, keys, self._old_keys)
        self._old_keys = keys
        self._screen.draw()

_app = None
def start_game():
    global _app
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init() #don't change the order of these or odd sound issues happen
    pygame.mixer.set_num_channels(8)
    menu_screen = menu.main_screen.MainScreen()
    _app = MyApp()
    _app.change_screen(menu_screen)
    _app.run()
    #start_screen(menu_screen)



def start_new_game():
     global _app
     _app.change_screen(tetris_screen.TetrisScreen())


def quit():
    pygame.quit()
    sys.exit()
