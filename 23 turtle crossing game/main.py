import time
from turtle import Screen
import random

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

RAN_Y = random.randint( -260, 260)


# Crear Scoreboard
# Colisiones

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")



game_is_on = True
while game_is_on:
    if player.ycor() > 270:
        player.turtle_repos()
        car_manager.move_increment()
        # aca va el incremento de lvl del score

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()



screen.exitonclick()