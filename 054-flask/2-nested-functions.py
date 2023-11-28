##Functions can be nested in other functions
# https://pythontutor.com/visualize.html#mode=display

def outer_function():
    print("I'm outer")

    # Indentation
    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()

