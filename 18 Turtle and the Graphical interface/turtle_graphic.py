### Day 18 ###
# La documentacion de la libreria esta en https://docs.python.org/3/library/turtle.html#
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("sea green")   # para ver los colores https://trinket.io/docs/colors

#
# for times in range (4): # hace un cuadrado
#     tim.forward(100) # el numero marca la distancia
#     tim.right(90) # el numero es los grados de giro

#
# for n in range (51): # Linea Punteada
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def random_pen_color():
    r = random.random()
    b = random.random()
    g = random.random()


    tim.pencolor(r,b,g)

# Challenge 3
form_angle = 3
while form_angle <11:
    random_pen_color()
    angle = 360 / form_angle
    for n in range (form_angle):
        tim.left(angle)
        tim.forward(100)
    form_angle += 1



screen = Screen()
screen.exitonclick()