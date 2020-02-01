from types import SimpleNamespace as MenuItem
import query
import gameloop
from . import menu_sounds
class MenuPlayer:
    def __init__(self):
        self.text = "Tetrominos"
        self.menu_items = [MenuItem(text="Start",selected=True, click = self.start_game), 
                           MenuItem(text="About",selected=False, click = self.about),
                           MenuItem(text="Quit",selected=False, click=self.quit)]
        self.selected_index = self.get_selected_index()
        self.sounds = menu_sounds.MenuSounds()
        self.sounds.menu_music()

    def get_selected_index(self):
        return [i for i in range(len(self.menu_items)) if self.menu_items[i].selected][0]


    def tick(self, ticks, controls, old_controls):
        if controls.menu_down and not old_controls.menu_down:
            self.sounds.menu_select()
            self.menu_items[self.selected_index].selected = False
            self.selected_index = (self.selected_index + 1) % len(self.menu_items)
            self.menu_items[self.selected_index].selected = True
            

        if controls.menu_up and not old_controls.menu_up:
            self.sounds.menu_select()
            self.menu_items[self.selected_index].selected = False
            self.selected_index = (self.selected_index - 1) % len(self.menu_items)
            self.menu_items[self.selected_index].selected = True


        if controls.menu_select and not old_controls.menu_select:
            selected = query.find_first(self.menu_items,lambda  x: x.selected == True)
            print(selected.text)
            selected.click()

    def start_game(self):
        print("Start game!")
        gameloop.start_new_game()

    def quit(self):
        gameloop.quit()
    
    def about(self):
        print("About!")
