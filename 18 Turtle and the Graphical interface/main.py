
# La documentación de la libreria está en https://docs.python.org/3/library/turtle.html#
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("sea green")   # para ver los colores https://trinket.io/docs/colors


def random_pen_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.pencolor(r,b,g)



tim.speed("fast")
tim.pensize(10)

directions = [0, 90, 180, 270]

for _ in range (100):
    random_pen_color()
    tim.forward(30)
    tim.setheading(random.choice(directions))








screen = Screen()
screen.exitonclick()