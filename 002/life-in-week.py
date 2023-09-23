# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left= 90 - float(age)
months_left = int(years_left * 12)
weeks_left = int(years_left * 52)
days_left = int(years_left * 365)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")