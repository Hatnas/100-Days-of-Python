import turtle

import random
from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("sea green")
turtle.colormode (255)
tim.penup()
tim.hideturtle()

# Requisitos
# 10 x 10 dots #
#de 20 con espacio de 50 #
# random color #
# siempre de izquierda a Derecha #

dots_color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]

def random_color():
    color = random.choice(dots_color_list)
    return color


def pattern():
    """ Hace una linea de 10 Dots de color random """
    for _ in range(10):
        tim.dot(20, random_color())
        tim.fd(50)


# Aca arranca el programa en si
y = -100
for _ in range (10):
    tim.teleport(-210, y)
    pattern()
    y += 30










screen = Screen()
screen.screensize(500, 500)
screen.exitonclick()