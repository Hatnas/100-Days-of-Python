import time
from turtle import Screen
import random

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

RAN_Y = random.randint( -260, 260)



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")


player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")


game_is_on = True
while game_is_on:
    if player.ycor() > 270:
        player.turtle_repos()
        car_manager.move_increment()
        score.lvl_up()

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #  Collision

    for car in car_manager.all_cars:
        if abs(car.ycor() - player.ycor()) <15:
            same_line = True
            if car.distance(player) < 25 and car.ycor():
                    game_is_on = False
                    score.game_over()




screen.exitonclick()