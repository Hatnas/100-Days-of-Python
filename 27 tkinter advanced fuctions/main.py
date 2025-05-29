
### TKINTER ###

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)    # Establezco el tamaño minimo de la ventana


## LABEL ##
# las lable son objetos dentro del modulo tkinter
# las Label tienen varios atributos

# Asi creo una Label pero no va a aparecer hasta que le diga como
my_label = Label(text= "I'm a Label", font=("Arial", 24, "bold"))
my_label.pack() # aca le estoy diciendo como quiero que aparezca por default pack va a top.

# pack documentation https://docs.python.org/3/library/tkinter.html#the-packer

# Puedo cambiar los atributos de Label como si fueran lo de un dicit
my_label["text"] = "New text"

# o como un kwargs
my_label.config(text = "Hola a todos")



## BUTTONS ##
# los botones tambien son objetos de una clase

def button_clicked():
    """ Al dar click cambia el texto de la etiqueta"""
    # my_label.config(text = "Button was clicked")
    my_label.config(text= input.get())
    

# Para que el boton detecte si fue clickeado hay que usar el arg command y darle una funcion pero SIN LOS PARENTESIS
button = Button(text= "Click me", command= button_clicked)
button.pack()


## ENTRY ##
# es basicamente un input que es un objeto dentro de tk

input = Entry(width=10)
input.pack()
input.get()   # Esta funcion es como un return. Me devuelve lo que haya en input y si no hay anda devuelve NONE


print ()

window.mainloop()      # Esta fucnion del objeto Window mantiene abierta la ventana



## D27 V10