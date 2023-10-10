from turtle import Turtle
import parameters as p


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color(p.SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 240)
        self.write(self.left_score, align=p.SCORE_ALIGN, font=(p.SCORE_FONT, p.SCORE_SIZE, 'normal'))
        self.goto(50, 240)
        self.write(self.right_score, align=p.SCORE_ALIGN, font=(p.SCORE_FONT, p.SCORE_SIZE, 'normal'))

    def increase(self, user="LEFT"):
        if user == "LEFT":
            self.left_score += 1
        else:
            self.right_score += 1
        self.update_scoreboard()