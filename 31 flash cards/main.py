from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"


# -------------------- Funciones ----------------- #
try:
    data = pandas.read_csv("Words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

french_list = data.to_dict(orient="records")  # lista de diccionarios Al usar "records" toma un valor de cada columna
current_card = {}


def random_card():
    global flip_timer, current_card

    window.after_cancel(flip_timer)
    current_card = random.choice(french_list)
    canvas.itemconfig(word_text, text= current_card["French"], fill= "black")
    canvas.itemconfig(language_text, text="French", fill= "black")
    canvas.itemconfig(canvas_image, image= c_front_image)

    flip_timer = window.after(3000, flip_card)


def flip_card():
     canvas.itemconfig(canvas_image, image = c_back_image)
     canvas.itemconfig(language_text, text= "English", fill= "white")
     canvas.itemconfig(word_text, text= current_card["English"], fill= "white")



# -------------------- Save Progress -------------- #
# delete and save
def correct():
    global french_list
    french_list.remove(current_card)
    new_data = pandas.DataFrame(french_list)
    new_data.to_csv("Words_to_learn.csv", index=False)
    random_card()


# --------------------- UI Setup ----------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)
window.minsize(width= 900, height= 600)
flip_timer = window.after(3000, flip_card)



# Canvas
canvas = Canvas(width= 800, height= 526,  bg= "#B1DDC6", highlightthickness=0)
c_front_image = PhotoImage(file="images/card_front.png")
c_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263 ,image= c_front_image)
canvas.grid(column=0, columnspan=2, row=0)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic" ))
word_text = canvas.create_text(400,263, text="Word", font=("Ariel", 60, "bold" ))




# Buttons

right_image = PhotoImage(file="images/right.png")
right_button = Button(image= right_image, highlightthickness=0, command= correct)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image= wrong_image, highlightthickness=0, command= random_card)
wrong_button.grid(row=1, column=0)


# --------------------- Ejecucion ----------------- #


random_card()


window.mainloop()


# -------- Falta ------------ #
# Armar las funciones para que cuando apreto correcto e incorrecto elimine o no la tarjeta de la lista!
# D31 V08