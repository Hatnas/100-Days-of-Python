import turtle

# para descargar el programa que toma los colores https://pypi.org/project/colorgram.py/
# import colorgram

## Para extraer los colores de la imagen

# colors = colorgram.extract('image.jpg' , 30)
#
#
# rgb_colors = []
#
# for color in colors:
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append (rgb)
#
# print (rgb_colors)


import random
from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("sea green")
turtle.colormode (255)

# Requisitos
# 10 x 10 dots
#de 20 con espacio de 50 #
# random color #
# siempre de izquierda a Derecha

dots_color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]

def random_color():
    color = random.choice(dots_color_list)
    return color

def dot(color):
    """ Esta funcion pone un Dot"""
    tim.pendown()
    tim.dot(20, color)

def fd():
    """ Mueve a la tortuga hacia adelante sin pintar"""
    tim.penup()
    tim.fd(50)

def pattern():
    """ Hace una linea de 10 Dots de color random """
    for _ in range(10):
        dot(random_color())
        fd()



# Aca arranca el programa en si
y = -250
for _ in range (10):
    tim.teleport(-300, y)
    pattern()
    y += 30










screen = Screen()
screen.screensize(500, 500)
screen.exitonclick()