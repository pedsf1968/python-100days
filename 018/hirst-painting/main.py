###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# https://pypi.org/project/colorgram.py/
import random
import colorgram
from turtle import Turtle, Screen


def find_colors_image(image, limit=30, white=240):
    """Get rgb colors from an image and remove white of the tuple list. limit is the length of the list
    and white the level of white color to remove"""
    rgb_colors = []
    colors = colorgram.extract(image, limit)
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        # Remove white
        if (red + green + blue)/3 < white:
            new_color = (red, green, blue)
            rgb_colors.append(new_color)
    return rgb_colors


def draw_dot_square(colors, length=10, width=20, spaces=50):
    """Draw a square of dots. length is the number of dots in a side, width is the size of the dot and spaces
     is the distance between two dots"""
    pointer = Turtle()
    pointer.shape("circle")
    pointer.speed("fastest")
    pointer.penup()
    pointer.setpos(-length*spaces/2, -length*spaces/2)
    for y in range(10):
        for x in range(10):
            pointer.pendown()
            pointer.dot(width, random.choice(colors))
            pointer.penup()
            pointer.setpos(x*spaces-length*spaces/2, y*spaces-length*spaces/2)


def main():
    screen = Screen()
    screen.colormode(255)
    rgb_colors = find_colors_image('image.jpg', 30)
    draw_dot_square(rgb_colors)
    screen.exitonclick()


if __name__ == '__main__':
    main()
