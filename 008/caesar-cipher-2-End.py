alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text.lower():
    index = alphabet.index(letter)
    index += shift_amount
    if index > len(alphabet):
      index -= len(alphabet)
    cipher_text += alphabet[index]

  print(f"The encoded text is {cipher_text}")

def decrypt(encoded_text, shift_amount):
  plain_text = ""
  for letter in encoded_text.lower():
    index = alphabet.index(letter)
    index -= shift_amount
    if index < 0:
      index += len(alphabet)
    plain_text += alphabet[index]

  print(f"The encoded text is {plain_text}")

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
else:
  decrypt(encoded_text=text, shift_amount=shift)