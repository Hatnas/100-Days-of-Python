
from turtle import Screen
from snake_class import Snake

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()

# ## Controles ##
# # Falta poner las flechas
#
# def turn_right():
#     segments[0].right(90)
#
# def turn_left():
#     segments[0].left(90)
#
# screen.listen()
# screen.onkey(fun= turn_right, key="d" )
# screen.onkey(fun= turn_left, key="a" )


# Aca arranca la ejecucion
snake.move()


















screen.exitonclick()