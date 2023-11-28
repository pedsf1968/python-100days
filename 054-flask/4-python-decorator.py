
## Simple Python Decorator Functions
import time


def delay_decorator(function):
    """need a function in argument"""
    def wrapper_function():
        """triger the function passed in argument"""
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")


say_hello()
say_bye()
say_greeting()


 # We can get new function construct by decorator and function in argument
decorated_function = delay_decorator(say_greeting)
decorated_function()


