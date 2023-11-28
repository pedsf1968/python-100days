import random
from art import logo,vs
from replit import clear
from game_data import data


def get_account(accounts):
    selected_account = random.choice(accounts)
    accounts.remove(selected_account)
    return selected_account

def print_question(account_compare, account_against):
    #clear()
    print(logo)
    print(f"Compare A: {account_compare['name']}, a {account_compare['description']}, from {account_compare['country']}.")
    print(vs)
    print(f"Against B: {account_against['name']}, a {account_against['description']}, from {account_against['country']}.")


def read_choice():
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice in ('A','B'):
        return choice
    else:
        read_choice()

def is_good_answer(answer, account_a, account_b):
    score_a = int(account_a['follower_count'])
    score_b = int(account_b['follower_count'])
    if answer == 'A' and score_a > score_b:
        return True
    if answer == 'B' and score_a < score_b:
        return True
    else:
        return False

accounts = data
continue_game = True
score = 0
account_compare = get_account(accounts)


while continue_game:
    account_against = get_account(accounts)
    print_question(account_compare, account_against)

    answer = read_choice()
    if is_good_answer(answer, account_compare, account_against):
        score += 0
        account_compare = account_against        
    else:
        continue_game = False

print(f"Sorry, that's wrong. Final score: {score}")


