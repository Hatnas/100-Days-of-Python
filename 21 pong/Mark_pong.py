from turtle import Turtle


class Mark(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.width(5)
        self.goto (0, -300)
        self.mid()




    def mid(self):
        self.setheading(90)
        for _ in range (0, 600):
            self.pendown()
            self.fd (10)
            self.penup()
            self.fd (10)

