
### US States Game

import turtle
import pandas
from States import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# Aca accedo al archivo
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()


correct_answer = []

# Arranca la ejecucion
while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50", prompt="State Name?").title()
    if answer_state == "Exit":
        state_left = [state for state in correct_answer if state_list not in correct_answer]
        missing_states = pandas.DataFrame(state_left)
        missing_states.to_csv("Missing states.csv")
        break

    if answer_state in state_list and answer_state not in correct_answer:
        state = State()
        state.correct(answer_state) # .item() devuelve un valor unico
                                    # y .iloc[n] devuelve el valor que este en n posicion
        correct_answer.append(answer_state)




### D25 V7





