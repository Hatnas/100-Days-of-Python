
#### Listeners ####

# Listeners es la forma en que el programa interactua con el usuario. Por ejemplo si aprata la flecha para arriba
# el personaje salta.
from turtle import Turtle,  Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("purple")


def move_forward():
    tim.forward(10)


        ### Higher order function ###
screen.listen()
screen.onkey( fun=move_forward, key="space" )  # necesito una funcion y una tecla
                                               # Cuando uso una funcion como input de otra funcion no lleva parentesis
                                               # La funcion principal se llama "Higher order function"


# Challenge 1 v 3
# Etch-a-Sketch






screen.exitonclick()

