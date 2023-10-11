from turtle import Turtle
from properties import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, SCREEN_HEIGHT_RANGE)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=SCORE_ALIGN, font=(SCORE_FONT, SCORE_FONT_SIZE, SCORE_FONT_TYPE))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.display()

    def increase(self):
        self.score += 1
        self.display()
