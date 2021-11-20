from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        physics_service (PhysicsService): An instance of PhysicsService.
    """

    def __init__(self, physics_service, audio_service):
        """The class constructor.
        
        Args:
            physics_service (PhysicsService): An instance of PhysicsService.
        """
        #super().__init__()
        self.physics_service = physics_service
        self.audio_service = audio_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        if self.physics_service.is_collision(ball, paddle):
            current_x = cast["balls"][0].get_velocity().get_x()
            reverse_y = cast["balls"][0].get_velocity().get_y() * -1
            cast["balls"][0].set_velocity(Point(current_x, reverse_y))

        for brick in bricks:
            if self.physics_service.is_collision(ball, brick):
                current_x = cast["balls"][0].get_velocity().get_x()
                reverse_y = cast["balls"][0].get_velocity().get_y() * -1
                cast["balls"][0].set_velocity(Point(current_x, reverse_y))
                bricks.remove(brick)
                self.audio_service.play_sound(constants.SOUND_BOUNCE)
        