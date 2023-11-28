# Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was
# given and finally the returned output:
#
# You called a_function(1,2,3)
# It returned: 6
# The value 6 is the return value of the function. Don't change the body of a_function.
#
# IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.
#
# Example Input
# [1,2,3]
# Example Output
# You called a_function(1,2,3)
# It returned: 6
# Hint
# You can use function.__name__ to get the name of the function.
#
# Use *args.

inputs = [1,2,3]
    # eval(input()))
# TODO: Create the logging_decorator() function 👇


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})"
                f"\nIt returned: {function(*args, **kwargs)}")
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c


a_function(inputs[0], inputs[1], inputs[2])