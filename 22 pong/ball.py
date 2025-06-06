import random
from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        ran_speed = [-10, 10]
        self.x_move = random.choice(ran_speed)
        self.y_move = random.choice(ran_speed)
        self.move_speed = 0.1


    # Move
    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor,new_ycor)


   # Bounce
    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1


    # Reset
    def reset(self):
        self.bounce_paddle()
        self.setposition(0, 0)
        self.move_speed = 0.1

    def speed_up(self):
        self.move_speed *= 0.9