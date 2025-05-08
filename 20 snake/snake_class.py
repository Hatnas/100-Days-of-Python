from turtle import Turtle,Screen

# ESTAS son variables constantes. Por eso estan en mayuscula
STARTER_POSITION  = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTER_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
            for num_seg in range(len(self.segments) - 1, 0,-1):  # con este For loop hago que todos se muevan a la posicion del anterior
                new_x = self.segments[num_seg - 1].xcor()
                new_y = self.segments[num_seg - 1].ycor()
                self.segments[num_seg].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

 ## Controles ##


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading (UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading (DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading (RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading (LEFT)


