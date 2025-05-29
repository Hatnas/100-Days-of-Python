from tkinter import *

def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)
window.config(padx= 20, pady= 20)

my_label = Label(text= "I'm a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)




button = Button()
button.config(text= "Im a button", command= button_clicked)
button.grid(column=1, row=1)

new_button = Button()
new_button.config(text="new button")
new_button.grid(column=3, row=0)

input = Entry(width= 10)
input.grid(column=4,row=2)








window.mainloop()