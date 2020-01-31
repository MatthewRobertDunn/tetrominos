import world
import renderer
import player

class TetrisScreen:
    def __init__(self):
           self.game = world.World(10, 20)
           self.p1 = player.Player(self.game)
           self.render = renderer.PyGameRenderer(self.game, self.p1)
 
    def tick(self, ticks, controls, old_controls):
        self.p1.tick(ticks,controls,old_controls)

    def draw(self):
        self.render.draw_tiles()
        self.render.draw_score()
