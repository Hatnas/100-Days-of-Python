from turtle import Turtle,Screen
import time



class Snake:
    def __init__(self):
        self.segments = []

        starting_position = [(0, 0), (-20, 0), (-40, 0)]

        for position in starting_position:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
        screen = Screen()
        game_is_on = True
        while game_is_on:
            screen.update()  # esto busca que los segmentos se muevan en bloque
            time.sleep(0.1)

            for num_seg in range(len(self.segments) - 1, 0,
                                 -1):  # con este For loop hago que todos se muevan a la posicion del anterior
                new_x = self.segments[num_seg - 1].xcor()
                new_y = self.segments[num_seg - 1].ycor()
                self.segments[num_seg].goto(new_x, new_y)
            self.segments[0].forward(20)
