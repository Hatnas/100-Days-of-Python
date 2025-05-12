
from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(5, 1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setpos(x= 350, y= 0)
        self.ycor()


## Controles
    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto (self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)




