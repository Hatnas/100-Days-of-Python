from turtle import Turtle

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(f"SCORE: {self.score}", False, "center", font=("Arial", 20, "normal"))

    def score_increase(self):
        self.clear()
        self.score += 1
        self.score_update()




