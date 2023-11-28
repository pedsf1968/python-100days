from turtle import Turtle
import random
from properties import *


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_wid=FOOD_STRETCH_WIDTH, stretch_len=FOOD_STRETCH_LENGTH)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-SCREEN_WITH_RANGE, SCREEN_WITH_RANGE)
        random_y = random.randint(-SCREEN_HEIGHT_RANGE, SCREEN_HEIGHT_RANGE)
        self.goto(random_x, random_y)

