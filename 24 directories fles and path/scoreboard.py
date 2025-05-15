from turtle import Turtle
ALIGNMENT= "center"
FONT= ("Courier", 20, "normal")

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.hideturtle()
        self.score_update()



    def score_update(self):
        self.clear()
        self.write(f"SCORE: {self.score}. HIGH SCORE: {self.high_score}", False, ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_update()

    #
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)

    def score_increase(self):
        self.score += 1
        self.score_update()





