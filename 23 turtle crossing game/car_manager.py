
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars =[]
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.speed("fastest")
            new_car.color(random.choice (COLORS))
            ran_y = random.randint(-250, 250)
            new_car.goto (300, ran_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def move_increment(self):
        self.move_speed += MOVE_INCREMENT

