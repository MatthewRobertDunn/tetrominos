from types import SimpleNamespace as MenuItem
class MenuPlayer:

    def __init__(self):
        self.menu_items = [MenuItem(Text="Start",Selected=True), 
                           MenuItem(Text="About",Seleced=False)]
