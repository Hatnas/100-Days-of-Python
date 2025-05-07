import turtle
# La documentación de la libreria está en https://docs.python.org/3/library/turtle.html#
import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("violet")   # para ver los colores https://trinket.io/docs/colors


def random_pen_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    tim.pencolor(r,b,g)


# Challenge 4
tim.speed("fastest")
tim.pensize(2)
#
# directions = [0, 90, 180, 270]
#
# for _ in range (100):
#     random_pen_color()
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# Challenge 5 Circulos

def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        random_pen_color()
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)

draw_spirograph(5)











screen = Screen()
screen.exitonclick()