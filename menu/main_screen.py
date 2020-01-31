import menu_player
import menu_renderer

class MainScreen:
    def __init__(self):
           self.p1 = menu_player.MenuPlayer()
           self.render = menu_renderer.MenuRenderer(self.p1)
 
    def tick(self, ticks, controls, old_controls):
        self.p1.tick(ticks, controls, old_controls)

    def draw(self):
        self.render.draw_tiles()
        self.render.draw_score()
