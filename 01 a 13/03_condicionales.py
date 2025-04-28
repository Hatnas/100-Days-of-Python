
### Dia 3 Rollercoaster ###

print ("Welcome to the rollercoaster")
height = int(input("Whats your height in cm?"))
bill = 0


if height >= 120:
    print ("You can ride!!!")
    age = int(input("How old are you?"))

    if age < 12:
        bill = 5
        print  ("Child tiket its, $5.")
    elif age <=18:
        bill = 7
        print  ("Teen tiket its, $7")
    else:
        bill = 12
        print  ("Adults tiket its, $12")

    wants_photo = input("Do you want the photo? Y or N")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3                                        #El valor de la foto es $3
    print (f"Your final bill is ${bill}")

else:
    print ("Sorry, you cant ride!! Too bad")
     

# PAR o IMPAR #

number = int(input ("Number"))

if number % 2 == 0:             # el % es un divisor modular, que nos permite ver si es completamente divisible o queda resto
    print ("El numero es PAR")
else:
    print ("El numero es IMPAR")


# Año Bisiesto (008) #

año = int (input("Cual es el año?"))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print ("Año Bisiesto")
        else:
            print ("Año no Bisiesto")
    else:
        print ("Año Bisiesto")
else:
    print ("Año no Bisiesto")



# Pizza Order (009) #

print ("Thanks you for choosing Python Pizza Deliveries!")
size = input("What size do you want? S, M, or L. ") # What size pizza do you want S, M, L
add_pepperoni = input("Add Pepperoni? Y or N. ") # Y o N
extra_cheese = input("Extra cheese? Y o N. ")  # Y o N

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
     if size == "S":
          bill += 2
     else:
          bill += 3

if extra_cheese == "Y":
    bill += 1

print (f"Your total bill is ${bill}")  



# Love Calculator #

name_1 = input("Cual es tu nombre? ")
name_2 = input("Cual es su nombre? ")
combined_names = name_1 + name_2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count ("l")
o = lower_names.count ("o")
v = lower_names.count ("v")
e = lower_names.count ("e")
second_digit = l + o + v + e

combined_leters = str(first_digit) +  str(second_digit)
x = int(combined_leters)

print ("The love calculator is calculating...")
if x < 10 or x > 90:
    print (f"Your score is {x}, you go together like Coke and Mentos")
elif x >= 40 and x <= 50:
    print (f"Your score is {x}, you ar allright together")
else:
    print (f"Your score is {x}")



# Tressure island #

print("Bienvenido a esta pseudo aventura donde tenes que decidir que opcion seguir.\nPara hacerlo tendras que escribir la decicion que prefieras.\nMucha suerte y esperemos que funcione.")
choice1 = input ("Estas en un cruce desde donde se abren dos caminos cual debes seguir? 'Izquierda' o 'Derecha'\n").lower()
if choice1 == "derecha":
    choice2 = input ("Te encuentras con un rio, puedes 'nadar' o 'esperar' a que pase un barco.\n").lower()
    if choice2 == "esperar":
        choice3 = input("Luego de cruzar el rio una cabaña con tres puertas numeradas se alsa ante ti\ que puerta cruzas? '1', '2' o '3'.\n")
        if choice3 == "1":
            print ("Activas una trampa el piso se abre bajo tus pies. Perdiste")
        elif choice3 == "2":
            print ("Encontras el tesoro secreto de Sarlanga, Ganaste")
        elif choice3 == "3":
            print ("No se... Perdiste porque la opcion era otra.")
        else:
            print ("Elegiste cualquier cosa.. era 1,2 o 3. Perdiste")
    else:
        print("te ahogas")
else:
    print ("Una abalancha te aplasta porque si... Perdiste.")

