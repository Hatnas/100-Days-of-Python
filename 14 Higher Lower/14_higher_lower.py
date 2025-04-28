
################################## Higher Lower ##############################################

from Higher_Lower import data
from Higher_Lower import vs
from Higher_Lower import logo
import random

data_list = data

def option():
    """ Genera aleatoreamente opciones dentro de la lista data"""
    option = random.choice(data_list)
    data_list.remove(option)
    return option

score = 0

def guess():
        global score
        global correct
        player_guess = input("Who has more followers 'A' or 'B'?:  ").lower()
        if player_guess == compare(option_a_followers,option_b_followers):
             score += 1
             print ("Correct!")
             print (f"Your score is {score}!")
             switch()
             
        else:
             print ("Wrong!")
             print (f"Your final score is {score}!")
             correct = False
             
def compare(option_a_followers, option_b_followers):
    if option_a_followers > option_b_followers:
        return "a"
    else:
        return "b"

def switch():
     global option_a_full
     global option_b_full
     if option_b_followers > option_a_followers:
         option_a_full = option_b_full
         option_b_full = option()    
     else:
          option_b_full = option()


print (logo)
again = True
while again == True:
    option_a_full = option()
    option_b_full = option()

    correct = True
    while correct == True:
        option_a_followers = int(option_a_full["follower_count"])
        option_b_followers = int(option_b_full["follower_count"])
        option_a = f"A: {option_a_full["name"]}, a {option_a_full["description"]} from {option_a_full["country"]}"
        option_b = f"B: {option_b_full["name"]}, a {option_b_full["description"]} from {option_b_full["country"]}"
        print (option_a)
        print (vs)
        print (option_b)

        guess()

    if (input("Whant to play adain? 'y' or 'n': ")).lower()!= "y":
        again = False
        print ("Good Bye!!!")

# Hacer un segundo dict donde se saquen los elementos que ya aparecieron