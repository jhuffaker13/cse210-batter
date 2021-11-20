import sys
from game import constants
import raylibpy

class GameOver():
    def _init_(self):
        self._textures = {}

    def gameover(self, audio_service, input_service):
        color = raylibpy.WHITE

        
        color = raylibpy.ORANGE
        text = "Game Over!"

        raylibpy.draw_text(text, 400, 300, constants.DEFAULT_FONT_SIZE, color)
        