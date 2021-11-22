from time import sleep

import raylibpy
from game import constants
from game.audio_service import AudioService
from game.input_service import InputService
from game.gameover import GameOver

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        self.audio_service = AudioService()
        self.input_service = InputService()
        self.game_over = GameOver()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            
                
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            # TODO: Add some logic like the following to handle game over conditions
            if len(self._cast["balls"]) == 0:  
                self.audio_service.play_sound(constants.SOUND_OVER)
                test_var = 0
                print("\nPress the SPACE BAR to close the game!\n")              
                while test_var == 0:
                    if self.input_service.is_space_pressed():
                        test_var = 1
                    #game_lost = True
                    
                    self._cue_action("output")
                    #self.game_over()

                self._keep_playing = False

            if raylibpy.window_should_close():
                self._keep_playing = False


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)