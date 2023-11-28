# Error types


try:
    a_dictionary = {"key": "value"}
    fruits = ["orange", "banana", "ananas"]
    text = "lkjhlk"

    # Line below rise a FileNotFoundError
    file = open("file.txt")

    # Line below rise a KeyError
    value = a_dictionary["key2"]

    # Line below rise a IndexError
    fruit = fruits[4]

    # Line below rise a TypeError
    print(text + 5)
except FileNotFoundError:
    # Simply catch the error
    print("ERROR: FileNotFoundError but we can create the file")
    file = open("file.txt", "w")
    file.write("Something")
except IndexError:
    print("ERROR: IndexError the length of list is 3, index can't be greater than 2 (0,1,2)")
except TypeError:
    print("ERROR: TypeError we can't add string and number")
except KeyError as error_message:
    # Catch the error and the message
    print(f"ERROR: Can't retreive data for {error_message} key!")
else:
    # if everything is OK
    content = file.read()
    print(content)
finally:
    # This always close the file
    file.close()
    # We rise an error
    # raise KeyError("I decide to rise an ERROR!")

# Sometimes we want to rise our own error
# If we want only human data for bmi calcul
height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)
