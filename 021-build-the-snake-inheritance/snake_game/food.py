from turtle import Turtle
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_MARGIN = 20
SCREEN_WITH_RANGE = int(SCREEN_WIDTH/2) - SCREEN_MARGIN
SCREEN_HEIGHT_RANGE = int(SCREEN_HEIGHT/2) - SCREEN_MARGIN
FOOD_COLOR = "purple"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-SCREEN_WITH_RANGE, SCREEN_WITH_RANGE)
        random_y = random.randint(-SCREEN_HEIGHT_RANGE, SCREEN_HEIGHT_RANGE)
        self.goto(random_x, random_y)

