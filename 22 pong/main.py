
### PONG ###

# Create Screen
# Create Paddle and move
# create 2nd PAddle
# Ball movement an wall collision (Bounce)
# Ball paddle collision (Bounce)
# Scoreboard detect paddle miss, keep score

from turtle import Screen
from net_pong import Net
from paddle_class import Paddle1, Paddle2
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

net = Net()
pad_r = Paddle1()
pad_l= Paddle2()
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(pad_r.go_up, "Up")
screen.onkey(pad_r.go_down, "Down")

screen.onkey(pad_l.go_up, "w")
screen.onkey( pad_l.go_down, "s" )


# Arranca la ejecución
game_in_on = True
while game_in_on:
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()

    #Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Collision With Paddles
    if ball.distance(pad_r) < 50 and  ball.xcor() > 350 or ball.distance(pad_l) < 50 and  ball.xcor() < -350:
        ball.bounce_paddle()
        ball.speed_up()


    # Punto Paddle R
    if ball.xcor() < -360:
        scoreboard.pad_r_point()
        ball.reset()

    # Punto Paddle L
    if ball.xcor() > 360:
        scoreboard.pad_l_point()
        ball.reset()






screen.exitonclick()
