from replit import clear
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount,cipher_direction):
  end_text = ""
  if cipher_direction == "encode":
    shift_amount *= -1

  for letter in start_text.lower():
    if letter in alphabet:
      index = alphabet.index(letter) + shift_amount
      if index > len(alphabet):
        index -= len(alphabet)
      elif index < 0:
        index += len(alphabet)
      end_text += alphabet[index]
    else:
      end_text += letter

  print(f"The encoded text is {end_text}")

end_of_game = False

while not end_of_game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  if input("Type 'yes' if you want to go again. Otherwise type 'no'.") == "no":
    end_of_game = True
  clear()