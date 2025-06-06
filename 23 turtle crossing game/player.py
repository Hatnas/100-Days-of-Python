from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_right(self):
        new_xcor = self.xcor() + 10
        self.goto(new_xcor, self.ycor())

    def move_left(self):
        new_xcor = self.xcor() - 10
        self.goto(new_xcor, self.ycor())

    def turtle_repos(self):
            self.goto(STARTING_POSITION)
