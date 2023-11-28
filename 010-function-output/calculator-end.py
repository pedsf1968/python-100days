from replit import clear
from art import logo

print(logo)

def addition(a,b):
    '''Return the addition of a and b'''
    return a + b

def substraction(a,b):
    '''Return the substraction of b to a'''
    return a - b

def multiplication(a,b):
    '''Return the product of a with b'''
    return a * b

def division(a,b):
    '''Return the division of a by b'''
    if b == 0:
        return "ERROR we can't divide by 0!"
    return a / b


operations = {
    "+": addition,
    "-": substraction,
    "*": multiplication,
    "/": division
}
        

def ask_operator():
    for symbol in operations:
        print(symbol)
    
    operator = input("Pick an operation: ")
    if operator in ("+","-","*","/"):
        return operator
    else:
        print(f"ERROR : {operator} is not an allowed operation!")
        return ask_operator()

def calculator():
    first_number = float(input("What's the first number?: "))
    new_calculation = True

    while new_calculation:
        operator = ask_operator()
        function = operations[operator]
        next_number = float(input("What's the next number?: "))
        result = function(first_number, next_number)

        print(f"{first_number} {operator} {next_number} = {result}")

        response = input(f"Type 'c' to continue calculating with {result}, or type 'n' to start a new calculation and anything to quit: ")
        if response == "c":
            first_number = result
        elif response == "s":
            clear()
            calculator()
        else:
            new_calculation = False


calculator()