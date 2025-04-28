
#### Day 12 ####

############## Scope #################

enemies = 1

def increase_enemies():
    enemies = 2
    print (f"enemies inside the funcion {enemies}")

increase_enemies()
print (f"enemies outside the funcion {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print (potion_strength)

drink_potion()
# print (potion_strength)  esto da error porque no esta definidio fuera de la funcion


### Python have NO BLOCK SCOPE  ###

# Las varialbes creadas dentro de IF, FOR o WHILE no tienen local scope a menos que esten dentro de una funcion
# de esa forma solo va a tener vigencia dentro de la misma funcion

game_level = 3
enemies = ["Skeletons", "Zombies", "Alien"]

if game_level < 5:                   # la funcion IF no tiene Local Scope. 
     new_enemy = enemies[0]          

print (new_enemy)  # esto va a dar de resultado Skeletons. 


### Modify Global Scope  ###

enemies = 1

def increase_enemies():
    global enemies                    # global marca una variable global para ser modificada dentro de una funcion
    enemies += 1
    print (f"enemies inside the funcion {enemies}")

increase_enemies()
print (f"enemies outside the funcion {enemies}")

# no es recomendable usar variables globales porque tiende a "enredar" el codigo
# es preferible hacer esto

enemies = 1

def increase_enemies():                   
    return enemies + 1

enemies = increase_enemies()
print (f"enemies outside the funcion {enemies}")


### Global Constants ###
# A veces queremos definir una variable global que va a ser "constante". Es decir que no vamos a modificar
# una buena forma de diferenciarlas es poniedola en MAYUSCULAS

VARIABLE_CONSTANTE = "Esto no lo quiero cambiar"

def turena():
    global VARIABLE_CONSTANTE 


######################################## Guess the number ###################################################
import random

logo = """
      ___         ___         ___         ___         ___                 
     /  /\       /__/\       /  /\       /  /\       /  /\                
    /  /:/_      \  \:\     /  /:/_     /  /:/_     /  /:/_               
   /  /:/ /\      \  \:\   /  /:/ /\   /  /:/ /\   /  /:/ /\              
  /  /:/_/::\ ___  \  \:\ /  /:/ /:/_ /  /:/ /::\ /  /:/ /::\             
 /__/:/__\/\:/__/\  \__\:/__/:/ /:/ //__/:/ /:/\:/__/:/ /:/\:\            
 \  \:\ /~~/:\  \:\ /  /:\  \:\/:/ /:\  \:\/:/~/:\  \:\/:/~/:/            
  \  \:\  /:/ \  \:\  /:/ \  \::/ /:/ \  \::/ /:/ \  \::/ /:/             
   \  \:\/:/   \  \:\/:/   \  \:\/:/   \__\/ /:/   \__\/ /:/              
    \  \::/     \  \::/     \  \::/      /__/:/      /__/:/               
     \__\/       \__\/       \__\/       \__\/       \__\/                
              ___         ___                                             
      ___    /__/\       /  /\                                            
     /  /\   \  \:\     /  /:/_                                           
    /  /:/    \__\:\   /  /:/ /\                                          
   /  /:/ ___ /  /::\ /  /:/ /:/_                                         
  /  /::\/__/\  /:/\:/__/:/ /:/ /\                                        
 /__/:/\:\  \:\/:/__\\  \:\/:/ /:/                                        
 \__\/  \:\  \::/     \  \::/ /:/                                         
      \  \:\  \:\      \  \:\/:/                                          
       \__\/\  \:\      \  \::/                                           
             \__\/       \__\/                                            
      ___         ___         ___                     ___         ___     
     /__/\       /__/\       /__/\       _____       /  /\       /  /\    
     \  \:\      \  \:\     |  |::\     /  /::\     /  /:/_     /  /::\   
      \  \:\      \  \:\    |  |:|:\   /  /:/\:\   /  /:/ /\   /  /:/\:\  
  _____\__\:\ ___  \  \:\ __|__|:|\:\ /  /:/~/::\ /  /:/ /:/_ /  /:/~/:/  
 /__/::::::::/__/\  \__\:/__/::::| \:/__/:/ /:/\:/__/:/ /:/ //__/:/ /:/___
 \  \:\~~\~~\\  \:\ /  /:\  \:\~~\__\\  \:\/:/~/:\  \:\/:/ /:\  \:\/:::::/
  \  \:\  ~~~ \  \:\  /:/ \  \:\      \  \::/ /:/ \  \::/ /:/ \  \::/~~~~ 
   \  \:\      \  \:\/:/   \  \:\      \  \:\/:/   \  \:\/:/   \  \:\     
    \  \:\      \  \::/     \  \:\      \  \::/     \  \::/     \  \:\    
     \__\/       \__\/       \__\/       \__\/       \__\/       \__\/    """
attempts = 0

def set_difficulty():
    difficulty = input("Choose a difficulty type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return attempts + 10
    else:
        return attempts + 5

def comparing (guess_number, random_number):
    global end_game
    if guess_number == random_number:
        print ("Correct, You win") 
        end_game = True
    elif guess_number < random_number:
        print ("Too low!")
    else:
        print ("Too high!")

print (logo)
play_again = True 
while play_again == True:   
    print ("Welcome to the Guess Number game.\n I will pick a number between 1 and 100")
    random_number = random.randint(1,100)
    attempts = set_difficulty() 
    print (f"You got {attempts} attempts")
    end_game = False
    while end_game == False:
        guess_number = int(input("Make a guess: "))
        if attempts > 1:
            comparing(guess_number,random_number)
            attempts -= 1
            if guess_number != random_number:
                print (f"you have {attempts} left")
        else:
            print ("Out of attempts, you lose!")
            print (f"The number was {random_number}")
            end_game = True
    if input("Whant to play again? 'y' or 'n': ").lower() != "y":
        end_game = False
