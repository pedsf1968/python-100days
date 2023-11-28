# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
# https://wrpsa.com/


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
ROCK_INDEX = 0
PAPER_INDEX = 1
SCISSORS_INDEX = 2
figures = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if human_choice < 0 or human_choice > 2:
    print("You typed an invalid number, you lose!")
else:
    print(figures[human_choice])
    print("Computer chose:\n")
    print(figures[computer_choice])

    if human_choice == computer_choice:
        print("It's a draw")
    elif  human_choice == ROCK_INDEX and computer_choice == SCISSORS_INDEX:
        print("You win!")
    elif human_choice == PAPER_INDEX and computer_choice == ROCK_INDEX:
        print("You win!")
    elif human_choice == SCISSORS_INDEX and computer_choice == PAPER_INDEX:
        print("You win!")
    else:
        print("You lose")
