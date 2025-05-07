from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)

colors = ["purple", "blue", "red", "orange", "green"]
y_position = [-120, -60, 0, 60, 120]
all_turtles =[]

race_on = False
user_bet = screen.textinput(title="Cawabonga!!!",prompt="¿Quien ganara la carrera? Purple, Red, Blue, Orange or Green").lower()

for turtle_index in range (0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print (f"You won. The winer is {winner_color}")
            else:
                print (f"You lose. The winer is {winner_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()