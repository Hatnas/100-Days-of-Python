
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


### Respuesta de la profesora ###


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = (random.choice(cards))
    return card
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
     return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():

  user_cards = []
  computer_cards = []
  user_cards.clear()
  computer_cards.clear()
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
