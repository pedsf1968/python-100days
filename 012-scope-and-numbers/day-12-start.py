################### Scope ####################

enemies = 1

def increase_enemies():
  # Never use the same name for local and global variables
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope
def drink_potion():
  # Variable potion_strength is local
  potion_strength = 2
  print(potion_strength)

# Error potion_strength isn't defined
# print(potion_strength)

# Global scope
# Variable player_health is global
player_health = 10

def drink_potion2():
  potion_strength = 2
  print(potion_strength)
  # Variable player_health is known because is global
  print(player_health)

# Error potion_strength isn't defined
# print(potion_strength)
# Variable player_health is known because is global
print(player_health)

# No block scope
game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
   new_enemy = enemies[0]

print(new_enemy)

# Modify global variables in function is not recommended
def increase_enemies2():
    # Refer to global value to modify it
    global enemies
    enemies = 4
    print(f"enemies inside function: {enemies}")

increase_enemies2()
print(f"enemies outside function: {enemies}")

#
def increase_enemies3():
    # Refer to global value to modify it
    print(f"enemies inside function: {enemies}")
    return enemies + 5

enemies = increase_enemies3()
print(f"enemies outside function: {enemies}")