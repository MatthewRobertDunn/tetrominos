from types import SimpleNamespace as MenuItem

class MenuPlayer:
    def __init__(self):
        self.Text = "Tetrominos!"
        self.menu_items = [MenuItem(Text="Start",Selected=True), 
                           MenuItem(Text="About",Selected=False)]
        self.selected_index = self.get_selected_index()
    

    def get_selected_index(self):
        return [i for i in range(len(self.menu_items)) if self.menu_items[i].Selected][0]


    def tick(self, ticks, controls, old_controls):
        if controls.menu_down and not old_controls.menu_down:
            self.menu_items[self.selected_index].Selected = False
            self.selected_index = (self.selected_index + 1) % len(self.menu_items)
            self.menu_items[self.selected_index].Selected = True

        return
