
import pandas
from turtle import Turtle
FONT = ("Courier", 8, "normal")

data = pandas.read_csv("50_states.csv")


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()


    def correct(self, state):
        """Coloca el nombre del estado en su lugar en el mapa"""
        state_row = (data[data.state == state])
        name = state_row.state.item()
        x = state_row.iloc[0].x
        y = state_row.iloc[0].y
        self.setpos(x, y)
        self.write(f"{name}", False, "center", FONT)



