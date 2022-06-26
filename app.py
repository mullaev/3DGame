from direct.showbase.ShowBase import ShowBase
from mapmanager import *
from hero import *

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        self.hero = Hero((2,3, 1), self.land)
        base.camLens.setFov(90)

game = Game()
game.run()

