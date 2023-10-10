from turtle import Turtle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_MARGIN = 20
SCREEN_WITH_RANGE = int(SCREEN_WIDTH/2) - SCREEN_MARGIN
SCREEN_HEIGHT_RANGE = int(SCREEN_HEIGHT/2) - SCREEN_MARGIN

SCORE_COLOR = "white"
SCORE_FONT = "Arial"
SCORE_SIZE = 12
SCORE_ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, SCREEN_HEIGHT_RANGE)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", align=SCORE_ALIGN, font=(SCORE_FONT, SCORE_SIZE, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=SCORE_ALIGN, font=(SCORE_FONT, SCORE_SIZE, 'normal'))

    def increase(self):
        self.score += 1
        self.display()
