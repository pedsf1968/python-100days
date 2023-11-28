from turtle import Turtle, Screen
import random

turtle_colors = ["green", "forest green", "dark green", "sea green","yellow", "gold", "orange", "red", "maroon",
                 "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen",
                 "chocolate", "brown", "black", "gray"]


def object_move(object):
    object.forward(100)
    object.right(90)


def object_draw_square(object, length):
    for _ in range(4):
        object.forward(length)
        object.right(90)


def object_draw_dashed_line(object, section=10, length=100):
    while section < length:
        object.forward(section)
        object.penup()
        object.forward(section)
        object.pendown()
        length -= 2 * section


def object_draw_polygone(object, sides=4, length=100):
    angle = 360 / sides
    for _ in range(sides):
        object.forward(length)
        object.right(angle)


def object_draw_multi_polygones(object, length=10):
    for sides in range(3, 10):
        object.color(random.choice(turtle_colors))
        object_draw_polygone(object, sides, length)

def random_rgb_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


def object_random_walk(object, length=20, rounds=200):
    directions = [0, 90, 180, 270]
    object.pensize(10)
    object.speed("fastest")
    for _ in range(rounds):
        object.color(random_rgb_color())
        object.forward(length)
        object.setheading(random.choice(directions))

def object_draw_spirograph(object, width=150, divisions=36):
    object.home()
    object.shape("classic")
    object.position()
    object.speed("fastest")
    angle = 0
    for _ in range(divisions+1):
        object.color(random_rgb_color())
        object.circle(width)
        object.setheading(angle)
        angle += 360/divisions


def main():
    timmy_the_turtle = Turtle()
    timmy_the_turtle.shape("turtle")
    screen = Screen()
    screen.colormode(255)

    # timmy_the_turtle.color(random.choice(turtle_colors))

    # object_move(timmy_the_turtle)
    # object_draw_square(timmy_the_turtle, 100)
    # object_draw_dashed_line(timmy_the_turtle, 10, 200)
    # object_draw_polygone(timmy_the_turtle, 3, 100)
    # object_draw_multi_polygones(timmy_the_turtle, 100)
    # object_random_walk(timmy_the_turtle, 20)
    object_draw_spirograph(timmy_the_turtle, 100, 72)

    screen.exitonclick()

if __name__ == '__main__':
    main()
