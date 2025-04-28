########## BLACK JACK ###########
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand_list = []
dealer_hand_list = []

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def add_card_dealer():
    dealer_hand_list.append(random.choice(cards))
    total_dealer_hand = sum(dealer_hand_list)

    num_aces = dealer_hand_list.count(11)  # Esta parte la arme con GPT     
    while total_dealer_hand > 21 and num_aces > 0:
        total_dealer_hand -= 10
        num_aces -= 1  # hasta aca
    
    if total_dealer_hand < 17:
        return add_card_dealer()
    else:
        print (f"The Dealer hand is {dealer_hand_list}, with a total of {total_dealer_hand}")
        return total_dealer_hand


def add_card():
    player_hand_list.append(random.choice(cards))
    total_player_hand = sum(player_hand_list)
    num_aces = player_hand_list.count(11)
    while total_player_hand > 21 and num_aces > 0:
        total_player_hand -= 10
        num_aces -= 1

    print (f"Your hand is {player_hand_list}, with a total of {total_player_hand}")
    return total_player_hand


def start_game():
    player_hand_list.clear()
    dealer_hand_list.clear()
    for card in range (2):
        player_hand_list.append(random.choice(cards))
        total_player_hand = sum(player_hand_list)
    dealer_hand_list.append(random.choice(cards))
    total_dealer_hand = sum(dealer_hand_list)
    print (f"Your hand is {player_hand_list}, with a total of {total_player_hand}")
    print (f"Dealer hand is {dealer_hand_list}, with a total of {total_dealer_hand}")




print (logo)
start = input ("Welcome to Leito's Black Jack. Whant to play?: 'y' or 'n' ")
if start == "y":
    start_game()
    if sum(player_hand_list)== 21 and len(player_hand_list)== 2:
        print ("Black Jack. You win")
    else:
        game_on = True
        while game_on == True:
            extra_card = True
            while extra_card == True:
                one_more_card = input("Whant another card?: 'y' or 'n': ").lower()
                if one_more_card == "y":
                    add_card()
                    if sum(player_hand_list)> 21:
                        extra_card = False
                        print ("You Lose!")
                else:   
                    extra_card = False

            ### El Dealer solo juega si el player no se pasa ###
                # asi establezco los valores totales para comprarlos despues
            if sum(player_hand_list) <=21:
                total_dealer_hand = add_card_dealer()   # Uso el return de la funcion (no llamo al Sum porque la lista tiene solo un valor)
                total_player_hand = sum(player_hand_list)

                if total_dealer_hand == 21 and len(dealer_hand_list)== 2:
                    print ("Black Jack. You Lose")
                elif total_player_hand > total_dealer_hand:
                    print ("You win!")
                elif total_dealer_hand > 21:
                    print ("You Win!")
                elif total_player_hand == total_dealer_hand:
                    print ("Draw!")
                else:
                    print ("You Lose!")    
        
            again = input ("Whant to play again? 'y' or 'n': ")
            if again == "y":
                start_game()
            else:
                game_on = False 
                print ("Good Bye!!")

else:
    print ("Good Bye!!")
