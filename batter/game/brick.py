from game.actor import Actor
from game import constants
from game.point import Point

class Brick(Actor):
    def __init__(self):
        super().__init__()    
        #self._position = ""
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)
        self.set_image(constants.IMAGE_BRICK)
        
        


        
