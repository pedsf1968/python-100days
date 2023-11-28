#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(f"\n{fruits}")

# For loop with range the 10 first numbers
for number in range(1,11):
  print(number)

# Add step
for number in range(1,11,3):
  print(number)

# Add all numbers of 1 to 100
total = 0
for number in range(1,101):
  total+=number

print("Total of numbers between 1 to 100: ",total)