from turtle import Turtle

ALIGNMENT= "center"
FONT= ("Courier", 30, "normal")

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.pad_r_score= 0
        self.pad_l_score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 250)
        self.hideturtle()
        self.score_update()


    def score_update(self):
        self.write(f" {self.pad_l_score}           {self.pad_r_score}", False, ALIGNMENT, font=FONT)



    def pad_l_point(self):
        self.clear()
        self.pad_l_score += 1
        self.score_update()

    def pad_r_point(self):
        self.clear()
        self.pad_r_score += 1
        self.score_update()