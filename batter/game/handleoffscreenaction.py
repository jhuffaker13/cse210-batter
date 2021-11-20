from game import constants
from game.action import Action
from game.ball import Ball
from game.point import Point

class HandleOffScreenAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0]
        balls = cast["balls"]
        for group in cast.values():
            current_y = cast["balls"][0].get_velocity().get_y()
            if cast["balls"][0].get_position().get_x() < 5:
                cast["balls"][0].set_velocity(Point(constants.BALL_DX, current_y))
            if cast["balls"][0].get_position().get_x() > 790:
                cast["balls"][0].set_velocity(Point(constants.BALL_DX * -1, current_y))
            if cast["balls"][0].get_position().get_y() < 5:
                reverse_x = cast["balls"][0].get_velocity().get_x()
                cast["balls"][0].set_velocity(Point(reverse_x, constants.BALL_DY * -1))
            if cast["balls"][0].get_position().get_y() > 595:
                balls.remove(ball)
                break