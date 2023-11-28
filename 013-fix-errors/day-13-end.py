############DEBUGGING#####################

# Describe Problem 
# change range from 20 to 21 because older loop can't reach 20 to print message
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

# Reproduce the Bug
# Range start at 1 and end to 6 but index is between 0 to 5
# change 1 to 0 and 6 to 5
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
# 1994 is not included change > with >= in the last condition
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
   print("You are a millenial.")
elif year >= 1994:
   print("You are a Gen Z.")

# Fix the Errors
# - Indentation error 
# - convert age to int
# - use f to format print
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# Print is Your Friend
# use == for assigning value
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages: {pages}")
print(f"word_per_page: {word_per_page}")
print(total_words)

# Use a Debugger
# identation in line 52, append after the loop
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])