
# Step 9 Target
import random

word_list = ("ardvark", "baboon", "camel")
chosen_word = random.choice(word_list)

display = []     
for letter in chosen_word:
    display += "_"

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
stages.reverse()


print (display)


end_of_game = False      #Creo una variable para terminar el juego
lives = 6

while not end_of_game:
    gess = input("Guess a letter?\n").lower()

    for possition in range(len(chosen_word)): 
        letter = chosen_word[possition]
        if letter == gess:
         display[possition] = letter
    print (f"{"".join(display)}")    # Uno todos los elementos de "display" en un str

    if gess not in chosen_word:
       stage_possition = lives
       print(f"You gessed {gess}, is not in the word!. You lose a li")
       print(stages[stage_possition])
       lives -=1
       if stage_possition == 0:
          end_of_game = True
          print ("You lose!!!")
       print (f"{"".join(display)}")    # Uno todos los elementos de "display" en un str
       

    if "_" not in display:
       end_of_game = True     # Cambio la variable
       print("You Win!!!")
