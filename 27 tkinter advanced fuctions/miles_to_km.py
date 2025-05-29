# Ejercico miles to km

# no se por que me sale la respuesta entre {}..
# video 12

from tkinter import *


def miles_to_km(a):
    km = a * 1.6
    return km

def answer():
    miles_input = int(entry.get())
    km_answer = {miles_to_km(miles_input)}
    km_conv["text"]= f"{km_answer}"

window = Tk()
window.minsize(width= 200, height= 100)
window.config(padx=20, pady=20)

# entry
entry= Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# label miles
miles_label = Label(text= "Miles")
miles_label.grid(column=2, row=0)

# label is equal to
equal_label = Label(text= "is equal to ")
equal_label.grid(column=0, row=1)

#label con los km convertidos
km_conv = Label(text= "0")
km_conv.grid(column=1, row=1)

# label Km
km_label = Label(text= "Km")
km_label.grid(column=2, row=1)

#button calculate
button = Button(text= "Convert", command= answer)
button.grid(column=2, row=2)








window.mainloop()