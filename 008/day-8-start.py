# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def great():
    print("\nHello Paul-Emmanuel")
    print("How do you do?")
    print("Isn't the weather nice today?")

great()

# Function that allow for input
def greet_with_name(name):
    print(f"\nHello {name}")
    print(f"How do you do {name}?")

greet_with_name("Paul-Emmanuel")

def greet_with(name, location):
    print(f"\nHello {name}")
    print(f"What is it like in {location}?")

greet_with("Paul-Emmanuel", "Seoul")
# With named arguments
greet_with(name="Paul-Emmanuel", location="Seoul")
