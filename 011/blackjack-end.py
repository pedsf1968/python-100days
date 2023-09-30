############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
import random
from os import system
from art import logo

def distribute_n_cards(cards, number=1):
    '''Pick n cards in a game and return them'''
    selected_cards = []
    if number > len(cards):
        number = len(cards)
    elif number < 1:
        number = 1
    for _ in range(number):
        card = random.choice(cards)
        selected_cards.append(card)
        cards.remove(card)
    return selected_cards

def continue_game():
    '''Return True if the user want to continue or False to stop'''
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        continue_game()

def get_score(cards):
    '''Calculate the best score between cards'''
    score = sum(cards)
    # Case of Black Jack Ace and figure
    if score == 21 and len(cards) ==2:
        return 0
    # Case of score upper 21 with Ace
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score -= 10
    return score

def display_current_score(player_cards, player_score, dealer_cards):
    '''Display curent state with player score'''
    print(f"\tYour cards: {player_cards}, current score: {player_score}")
    print(f"\tComputer's first card: {dealer_cards[0]}")

def display_final_score(player_cards, player_score, dealer_cards, dealer_score):
    '''Display final scores with emoji'''
    print(f"\tYour final hand: {player_cards}, final score: {player_score}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")
    if player_score == 21:
        print("You win 😃")
    elif dealer_score == 21:
        print("You lose 😤")
    elif dealer_score > 21:
        print("Opponent went over. You win 😁")
    elif player_score > 21:
        print("You went over. You lose 😭")
    elif player_score == dealer_score:
        print("Draw 🙃")
    elif player_score > dealer_score:
        print("You win 😃")
    elif player_score < dealer_score:
        print("You lose 😤")

def match_continue(player_score, dealer_score):
    '''Test if the game is over'''
    if player_score == 21 or dealer_score == 21 or player_score > 21:
        return False
    else:
        return True


def play_game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    dealer_hand = []
    player_hand.extend(distribute_n_cards(cards, 2))
    dealer_hand.extend(distribute_n_cards(cards, 2))
    want_a_card = True
    match_endded = False

    while not match_endded:
        player_score = get_score(player_hand)
        dealer_score = get_score(dealer_hand)
        display_current_score(player_hand, player_score, dealer_hand)
        
        if match_continue(player_score, dealer_score):
            if input(f"Type 'y' to get another card, type 'n' to pass: ") == "y":
                player_hand.extend(distribute_n_cards(cards))
                player_score = get_score(player_hand)
            else:
                match_endded = True    
        else:
            match_endded = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.extend(distribute_n_cards(cards))       
        dealer_score = get_score(dealer_hand)    

    display_final_score(player_hand, player_score, dealer_hand, dealer_score)


while continue_game():
    system('cls')
    play_game()

            

