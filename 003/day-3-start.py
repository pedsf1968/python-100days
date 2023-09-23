print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
      bill = 5
      print("Child tickets are ${bill}.")
    elif age <= 18:
      bill = 7
      print("Youth tickets are ${bill}.")
    elif age >= 45 and age <= 55:
      print("Everything is going to be ok. Have a ride on us!")
    else:
        bill = 12
        print("Adult tickets are ${bill}.")

    whant_photo = input("Do you whant a photo taken? Y or N. ")
    if whant_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
