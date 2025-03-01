from game.actor import Actor
from game import constants
from game.point import Point

class Paddle(Actor):
    def __init__(self):
        super().__init__()    
        #self._position = ""
        self.set_width(constants.PADDLE_WIDTH)
        self.set_height(constants.PADDLE_HEIGHT)
        self.set_image(constants.IMAGE_PADDLE)