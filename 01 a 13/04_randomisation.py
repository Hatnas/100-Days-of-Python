
### Randomisation and Lists ###

from random import randint

# Flip a Coin #

      #Creo una Lista
coin =["Head", "Tail"]    
      #creo una variable random
coin_flip = randint(1,2)   

if coin_flip == 1:
    #Llamo al elemnto de la lista por orden
    print (coin[0])
else:
    print (coin[1])




# Banker Roulet (005) #

names = []

names.append(input("Nombre1\n"))
names.append(input("Nombre2\n"))
names.append(input("Nombre3\n"))
names.append(input("Nombre4\n"))
names.append(input("Nombre5\n"))

names_number = len(names)
random_choice = randint(0, names_number-1)

print (names[random_choice], "Invites diner!")


# Nesting a List into another List (006) #

fruits = ["Frutillas", "Manzanas", "Bananas"]
vegetables = ["Lechuga", "Papa", "Batata"]

full_list = [fruits, vegetables]       # Esto me hacer una Lista de Listas, se veria algo asi [[Fritillas, Manzanas, Bananas][Lechuga, Papa, Batata]]



# Tresure Map (008)
line1 = ["-", "-", "-"]
line2 = ["-", "-", "-"]
line3 = ["-", "-", "-"]
map = [line1, line2, line3]
print ("Hiding your tresure! Mark X in the spot")
position = input()

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)

number_index = int(position [1]) -1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")



### Piedra, Papel y Tijera ###

ppyt = ["Piedra", "Papel", "Tijera"]

player_choice_int= int(input(''' Juguemos Piedra, Papel y Tijera
Escribi 0 si queres Piedra, 1 si queres Papel o 2 si queres Tijera\n  '''))

program_random = randint (0,2)
program_choice = ppyt[program_random]
if player_choice_int == 0 and program_random ==2:
    print ("Elijo", program_choice)
    print ("Ganaste")
elif program_random > player_choice_int:
    print ("Elijo", program_choice)
    print ("Perdiste")
elif program_random == 0 and player_choice_int ==2:
    print ("Elijo", program_choice)
    print ("Ganaste")
elif program_random < player_choice_int:
    print ("Elijo", program_choice)
    print ("Ganaste")
elif program_random == player_choice_int:
    print ("Elijo", program_choice)
    print ("Empatamos")
else:
    print("Elegiste un numero incorrecto")


### Ppyt Con Matriz ###
from random import randint

rock = ["Elijo Piedra: Empatamos", "Elijo Piedra: Ganaste", "Elijo Piedra: Perdiste "]
paper = ["Elijo Papel: Perdiste", "Elijo Papel: Empatamos", "Elijo Papel: Ganaste "]
sissors = ["Elijo Tijera: Ganaste", "Elijo Tijera: Perdiste", "Elijo Tijera: Empatamos "]
rpns = [rock, paper, sissors]


player_choice = int(input("Juguemos Piedra, Papel o Tijera.\n0: Piedra, 1: Papel o 2: Tijera\n"))
program_choice = randint(0,2)

print (rpns[program_choice][player_choice])

