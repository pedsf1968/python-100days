from turtle import Turtle
import parameters as p


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(p.SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(p.SCORE_X_POS, p.SCORE_Y_POS)
        self.write(f"Level: {self.score}", align=p.SCORE_ALIGN, font=(p.SCORE_FONT, p.SCORE_FONT_SIZE, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=(p.SCORE_FONT, p.SCORE_SIZE, 'normal'))
