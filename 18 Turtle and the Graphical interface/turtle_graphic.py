### Day 18 ###
# La documentación de la libreria está en https://docs.python.org/3/library/turtle.html#
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


# Challenge 3

def random_pen_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.pencolor(r,b,g)

# ### Random color Shape
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for n in range(num_side):
#         tim.left(angle)
#         tim.forward(100)
#
#
# # Aca arranca le ejecucion
# for shape in  range (3, 11):
#     random_pen_color()
#     draw_shape(shape)

#
# #### Challenge 5 ####
# orientation = 0
# for _ in range (70):
#     random_pen_color()
#     tim.setheading(orientation)
#     tim.circle(100)
#     orientation += 12






screen = Screen()
screen.exitonclick()