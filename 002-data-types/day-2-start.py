print("\nData Types")
print(len("Hello"))

# ERROR
# print(len(1234))

# String
print("\nString")
word = "Hello"
print(word)
print(type(word))
print("First character: " + word[0])
print("Last character: " + "Hello"[4])
print("Last character: " + "Hello"[-1])
print("123" + "345")

# Use str() to convert integer to String
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
print(str(19) + str(68))
# Integer
print("\nInteger")
# Sum 2 integers and display result
print(123 + 345)
print(123456789)
print(type(123456789))
# More easy to read large integers
print(123_456_789)

# Float
print("\nFloat")
print(3.14159)
print(type(3.14159))

# Use float() to convert String in float
print(70 + float("11.5"))

# Boolean
print("\nBoolean")
print(True)
print(type(True))
print(False)

print("\nMathématical opérations")
# Mathématical opérations
print("3 + 5 = ", 3 + 5, type(3 + 5))
print("7 - 4 = ", 7 - 4, type(7 - 4))
print("3 * 2 = ", 3 * 2, type(3 * 2))
print("6 / 5 = ", 6 / 5, type(6 / 5))
print("3 ** 2 = ", 3**2, type(3**2))

# PEMDAS priority
# Parenthesys ()
# Exponetial **
# Multiplication *
# Division /
# Addition +
# Substraction -
print("3 * 3 + 3 / 3 - 3 = ", 3 * 3 + 3 / 3 - 3)

# Number manipulations
print("\nNumber manipulations")
print("8 / 7 =", 8 / 3, type(8 / 3))
print("8 // 7 =", 8 // 3, type(8 // 3))
print("int(8/7) =", int(8 / 3))
print("round(8/7) =", round(8 / 3))
print("round(8/7,3) =", round(8 / 3, 3))

# Modify a number
score = 0
print("Score: ", score)
score += 3
print("Score + 3 : ", score)
score /= 2
print("Score / 2: ", score)
isWinning = True
# Other way to print strings and numbers together with f-string
print("score :", type(score))
print("isWinning :", type(isWinning))
print(f"Your score is {score}, are you winning? {isWinning}")
