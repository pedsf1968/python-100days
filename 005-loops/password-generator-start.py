#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nb_letters= int(input("How many letters would you like in your password?\n")) 
nb_symbols = int(input(f"How many symbols would you like?\n"))
nb_numbers = int(input(f"How many numbers would you like?\n"))
print(f"\nletter, {nb_symbols} symbol, {nb_symbols} number")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for l in range(1,nb_letters+1):
    password += random.choice(letters)

for s in range(1,nb_symbols+1):
    password += random.choice(symbols)

for n in range(1,nb_numbers+1):
    password += random.choice(numbers)

print(f"\nEazy Level - Order not randomised: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letter_types = ["LETTER","SYMBOL","NUMBER"]
password = ""

for c in range(1,nb_letters+nb_symbols+nb_numbers+1):
  char_type = random.choice(letter_types)
  if char_type == "LETTER":
    password += random.choice(letters)    
    nb_letters -= 1
    if nb_letters == 0:
       letter_types.remove("LETTER")
  elif char_type == "SYMBOL":
    password += random.choice(symbols)
    nb_symbols -= 1
    if nb_symbols == 0:
       letter_types.remove("SYMBOL")
  else:
    password += random.choice(numbers)
    nb_numbers -= 1
    if nb_numbers == 0:
       letter_types.remove("NUMBER")

print(f"\nHard Level - Order of characters randomised: {password}")
  

