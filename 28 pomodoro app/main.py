from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer ():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Para cambiar el texto de un canvas tengoque usar itemconfig(canvas_a_cambiar, atributo kw)
    if count >0:
        window.after(1000, count_down, count -1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)


canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness=0)
tomato = PhotoImage(file= "tomato.png")    # Para poder meter una imagen en el canvas la tengo que transformar en un
# objeto de la clase PhotoImage.
canvas.create_image(100, 112, image= tomato) # aca establezco la x, y e imagen del canvas
timer_text = canvas.create_text(100,130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold" ))
canvas.grid(column= 1, row= 1)


# Label Timer
timer_label = Label(text= "Timer",font=(FONT_NAME, 35, "bold"), fg=GREEN, bg= YELLOW)
timer_label.grid(column=1, row=0)


# button start
start_button = Button(text="Start", command= start_timer) #falta el command
start_button.grid(column=0, row=3)


#button reset
reset_button = Button(text= "Reset") #falta el command
reset_button.grid(column=3, row=3)


# label check
check_label = Label(text= "✔",fg=GREEN)
check_label.grid(column=1, row=4)




window.mainloop()