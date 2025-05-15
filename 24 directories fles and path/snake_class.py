from turtle import Turtle

# ESTAS son variables constantes. Por eso están en mayúscula
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
            self.add_segment(position)


    def add_segment(self, position):
        ext_seg = Turtle(shape="square")
        ext_seg.penup()
        ext_seg.color("white")
        ext_seg.goto(position)
        self.segments.append(ext_seg)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
            for num_seg in range(len(self.segments) - 1, 0,-1):  # con este For loop hago que todos se muevan a la posición del anterior
                new_x = self.segments[num_seg - 1].xcor()
                new_y = self.segments[num_seg - 1].ycor()
                self.segments[num_seg].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

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


