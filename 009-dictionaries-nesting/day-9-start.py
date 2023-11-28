programming_dictionary = { 
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again." 
    }

# Retrieving items from dictionnary.
print('programming_dictionary["Bug"]: ', programming_dictionary["Bug"])

# Change item value
programming_dictionary["Bug"] = "A moth in your computer."
print('programming_dictionary after changing "Bug": ',programming_dictionary)


# Adding new items to dictionnary.
programming_dictionary["Loop"] = "A piece of code that you can easily call over and over again."
print('programming_dictionary after adding "Loop": ',programming_dictionary)

# Loop through a dictionnary print only keys
for thing in programming_dictionary:
    print(thing)

# Loop through a dictionnary print keys and values
for key in programming_dictionary:
    print(key, ":", programming_dictionary[key])


# Create empty dictionnary.
empty_dictionnary = {}

# Reset dictionnary
programming_dictionary = {}
print("programming_dictionary after reset:",programming_dictionary)

