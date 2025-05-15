
from turtle import Turtle
import random


class Food (Turtle):             # Para que una clase Herede de otra. La Superclase va entre parentesis
    def __init__(self):
        super().__init__()          # Dentro de la construccion de la clase se estblece que Hereda de otra Super
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("violet")
        self.speed("fastest")
        self.spam()


    def spam (self):
        ran_x = random.randint(-270, 270)
        ran_y = random.randint(-270, 270)
        self.goto(x= ran_x, y= ran_y)