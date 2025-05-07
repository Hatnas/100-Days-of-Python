import turtle
# Video 3 Challenge 1

# Etch a Sketch

from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("purple")
tim.pensize(5)

# Hay que usar listeners para poder
# w = avanzar
# s = retroceder
# A = girar hacia la izq
# D = girar a la derecha
# C = Clear y volver al centro

# Chequear si hay unn While press

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.teleport(0,0)

screen.listen()
screen.onkey(fun=forward, key="w" )
screen.onkey(fun=backward, key="s" )
screen.onkey(fun=turn_left, key="a" )
screen.onkey(fun=turn_right, key="d" )
screen.onkey(fun=clear, key="c" )





screen.exitonclick()