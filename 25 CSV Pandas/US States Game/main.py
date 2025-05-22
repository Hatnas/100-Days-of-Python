
### US States Game

# Si la respuesta es correcta
# colocar el nombre en las coordenadas correspodnientes
# Sumar 1 al total de estados adivinados


import turtle
import pandas
from States import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state = State()

# Aca accedo al archivo
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

correct_answer = []
score = len(correct_answer)
game_on = True
while game_on:
    score = len(correct_answer)
    answer_state = screen.textinput(title=f"{score}/50", prompt="State Name?").title()
    if answer_state in state_list and answer_state not in correct_answer:
        state.correct(answer_state)
        correct_answer.append(answer_state)

    if score == 50:
        game_on = False





correct_answer_list = []







turtle.mainloop()