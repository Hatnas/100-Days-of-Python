
### PONG ###

# Create Screen
# Create Paddle and move
# create 2nd PAddle
# Ball movement an wall collision (Bounce)
# Ball paddle collision (Bounce)
# Scoreboard detect paddle miss, keep score

from turtle import Screen
from Mark_pong import Mark
from paddle_class import Paddle1
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)          # Tengo quilombo con el refresh

mark = Mark()
pad1 = Paddle1()
#pad2 = Paddle2()





screen.listen()
screen.onkey(pad1.go_up, "Up")
screen.onkey( pad1.go_down, "Down" )

game_in_on = True
while game_in_on:
    screen.update()


screen.exitonclick()