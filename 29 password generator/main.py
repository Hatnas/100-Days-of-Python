from tkinter import *
from tkinter import messagebox
from random import choice, shuffle,randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for s in range(randint(2, 4))]
    password_numbers = [choice(numbers) for s in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web = website_entry.get()
    user = email_user_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oooopsss", message= "Please don't leave any field empty...")

    else:
        is_ok = messagebox.askokcancel(title = web, message= f"This are de details entered \nEmail/User: {user}\n"
                                                     f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("Passwords.txt", "a") as f:
                f.write(f"{web} | {user} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

## Window ##
window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)


## Canvas ##
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= logo)
canvas.grid(column= 1, row= 0)

## Labels ##
website_label = Label(text= "Website: ")
website_label.grid(column=0, row=1)

email_user_label = Label(text= "Email/Username: ")
email_user_label.grid(column=0, row=2)


password_lable = Label(text= "Password: ")
password_lable.grid(column=0, row=3)


## Entry ##
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row= 1, columnspan=2)


email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row= 2, columnspan=2)
email_user_entry.insert(0, "leonardo.mastrnagelo@gmail.com")

password_entry= Entry(width=17)
password_entry.grid(column=1, row=3)

## Button ##
generate_pass = Button(text= "Generate Password", command= generate_password)
generate_pass.grid(column=2, row= 3)

add = Button(text= "Add", width=36, command= save_password, )
add.grid(column=1, row=4, columnspan=2)



window.mainloop()