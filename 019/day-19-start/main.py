from turtle import Turtle, Screen
import random

pointer = Turtle()
screen = Screen()

def move_forwards():
    pointer.forward(10)


def move_backwards():
    pointer.backward(10)


def move_counter_clockwise():
    angle = pointer.heading() + 10
    if angle > 360:
        angle -= 360
    pointer.setheading(angle)


def move_clockwise():
    angle = pointer.heading() - 10
    if angle < -360:
        angle += 360
    pointer.setheading(angle)


def clear():
    pointer.clear()
    pointer.penup()
    pointer.home()
    pointer.pendown()


def main():
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=move_counter_clockwise)
    screen.onkey(key="d", fun=move_clockwise)
    screen.onkey(key="c", fun=clear)
    screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()