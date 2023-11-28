# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors

from turtle import Turtle, Screen
from prettytable import PrettyTable
import another_module


def use_turtle_module():
    # Call the constructor of object Turtle
    timmy = Turtle()
    print(timmy)
    timmy.shape("turtle")
    timmy.color("Chartreuse3")
    timmy.forward(100)

    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick()


def use_prettytable():
    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])
    table.align = "l"
    print(table)


if __name__ == '__main__':
    print(another_module.another_variable)
    use_turtle_module()
    use_prettytable()
