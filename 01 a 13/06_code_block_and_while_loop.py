### 06 Code block and While loop ###

# Regorb Hurdle1

"""
pagina: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for steps in range(6):
    jump()
"""

# While loop
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

  
number_of_hurdle = 6
while number_of_hurdle >0:
    jump()
    number_of_hurdle -= 1
    print(number_of_hurdle)

# Random goal
while not at_goal():
    jump()
    """

# Hurdle 3
  # https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json


# Hudle 4 
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()       
    turn_right()
    move()
    turn_right()       
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
"""

# Ejercicio final (009)
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
     
    # La solucion de la profe
while not at_goal():
    if righ_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

"""


