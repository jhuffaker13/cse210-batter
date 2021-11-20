import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.controlactorsaction import ControlActorsAction
from game.handlecollisionsaction import HandleCollisionsAction
from game.handleoffscreenaction import HandleOffScreenAction
from game.moveactorsaction import MoveActorsAction
from game.gameover import GameOver

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    cast['bricks'] = []
    bricks = []
    for i in range (15):
        for n in range(8):
            brick = Brick()
            position = Point(25+(i*50), 20+(n*30))
            brick.set_position(position)
            bricks.append(brick)
    cast["bricks"] = bricks
    # TODO: Create bricks here and add them to the list

    cast["balls"] = []
    balllist = []
    ball = Ball()
    position = Point(600, 300)
    ball.set_position(position)
    ball.set_velocity(Point(constants.BALL_DX, constants.BALL_DY))
    balllist.append(ball)
    cast["balls"] = balllist
    # TODO: Create a ball here and add it to the list

    cast["paddle"] = []
    paddlelist = []
    paddle = Paddle()
    position = Point (400, 550)
    paddle.set_position(position)
    paddlelist.append(paddle)
    cast["paddle"] = paddlelist
    # TODO: Create a paddle here and add it to the list
    ball.get_position().get_x()

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService(cast)
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service)


    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, handle_off_screen_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()
    audio_service.stop_audio()

if __name__ == "__main__":
    main()
