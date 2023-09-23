# A module is a python file that contain functions and variables
import my_module

# Call my module value
print(my_module.pi)

# Import random module to use random functions
import random

# Simple random integer between 1 to 10 and 1 and 10 are included
random_integer = random.randint(1, 10)
print(random_integer)

# Simple random float between 0.0 to 1.0 and 1.0 is not included
random_float = random.random()
print(random_float)

# Apply an other method for love score
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# List to store same type of datas in structured way
sk_provinces = [
    "Gyeongsangnam-do", "Gyeongsangbuk-do", "Jeollanam-do", "Jeollabuk-do",
    "Jeju Special Self-Governing Province", "Gangwon-do", "Chungcheongnam-do",
    "Chungcheongbuk-do", "Gyeonggi-do", "Chagang-do", "Hamgyongbok-do",
    "Hamgyonglam-do", "Whanghaebok-do", "Whanghaenam-do", "jangwon-do",
    "Pyonganbok-do", "Pyongannam-do", "Ryanggang-do"
]

print(f"\nAll regions of Korea \n{sk_provinces}")

# The first item is 0
print(f"\nThe first region is {sk_provinces[0]}")
print(f"The second region is {sk_provinces[1]}")

# Access the list in reverse with negative index
print(f"\nThe last region is {sk_provinces[-1]}")
print(f"The second last region is {sk_provinces[-2]}")

# Change an item in the list
print(f"The 5 region is {sk_provinces[4]}")
region_backup = sk_provinces[4]
sk_provinces[4] = "Bourgogne-Franche-Comté"
print(f"Now the 5 region is {sk_provinces[4]}")
sk_provinces[4] = region_backup

# Add new province with append()
sk_provinces.append("Bourgogne-Franche-Comté")
# Access the list in reverse with negative index
print(f"\nThe last region is {sk_provinces[-1]}")
print(f"The second last region is {sk_provinces[-2]}")

# Add several province with extend()
new_provinces = ["Hauts-de-France", "Occitanie", "Provence-Alpes-Côte-d'Azur"]
sk_provinces.extend(new_provinces)
print(f"\nAll new regions are \n{sk_provinces}")

# https://www.delish.com/food-news/a26872638/dirty-dozen-foods-list-2019/
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# It's a list of fruit and vegetables
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables  = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Create a nested list
dirty_dozen = [ fruits, vegetables]
print(f"\n {dirty_dozen}")
