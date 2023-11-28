#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
from art import logo

difficulties = {
    "hard": 5,
    "easy": 10,
}


def ask_difficulty():
    answer = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if answer in difficulties:
        return difficulties[answer]
    else:
        ask_difficulty()

def display_result():
    print("Too low.")
    print("Too high.")
    print("You have 9 attempts remaining to guess the number.")

def game_init():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def game():
    number_to_find = random.randint(0,100)
    print(f"Pssst, the correct answer is {number_to_find}")
    attempts = ask_difficulty()
    continue_game = True

    while continue_game:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_find:
            print(f"You got it! The answer was {number_to_find}.")
            continue_game = False
        else:
            attempts -= 1    
            if guess < number_to_find:
                print("Too low.")
            else:
                print("Too high.")
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                continue_game = False
            else:
                print("Guess again.")

game_init()
game()