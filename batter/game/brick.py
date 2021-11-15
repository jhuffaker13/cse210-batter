from game.actor import Actor
from game import constants

class Brick(Actor):
    def _init_(self):
        super.__init__()    
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)