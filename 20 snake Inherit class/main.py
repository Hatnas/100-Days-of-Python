
from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun= snake.up, key="Up")
screen.onkey(fun= snake.down, key="Down" )
screen.onkey(fun= snake.left, key="Left" )
screen.onkey(fun= snake.right, key="Right" )



# Aca arranca la ejecución

game_is_on = True
while game_is_on:
    screen.update()  # esto busca que los segmentos se muevan en bloque
    time.sleep(0.1)
    snake.move()


    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.spam()
        snake.extend()
        scoreboard.score_increase()


    # Detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False


    # Detect collision with head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


















screen.exitonclick()