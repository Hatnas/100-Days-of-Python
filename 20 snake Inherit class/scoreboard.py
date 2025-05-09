from turtle import Turtle
ALIGNMENT= "center"
FONT= ("Courier", 20, "normal")

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
        self.write(f"SCORE: {self.score}", False, ALIGNMENT, font= FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def score_increase(self):
        self.clear()
        self.score += 1
        self.score_update()




