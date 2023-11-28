from turtle import Turtle
import parameters as p


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color(p.PADDLE_COLOR)
        self.shapesize(stretch_wid=p.PADDLE_STRETCH_WIDTH, stretch_len=p.PADDLE_STRETCH_LENGTH)
        self.penup()
        self.goto(x_pos, 0)

    def up(self):
        """Move paddle up"""
        y_pos = self.ycor() + p.PADDLE_MOVE
        self.goto(self.xcor(), y_pos)

    def down(self):
        """Move paddle down"""
        y_pos = self.ycor() - p.PADDLE_MOVE
        self.goto(self.xcor(), y_pos)
