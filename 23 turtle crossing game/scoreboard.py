from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto( - 250,250 )
        self.speed("fastest")
        self.hideturtle()
        self.level = 1
        self.lvl()

    def lvl(self):
        self.write(f"LEVEL: {self.level}", False, "left", FONT)

    def lvl_up(self):
        self.clear()
        self.level += 1
        self.lvl()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", FONT)