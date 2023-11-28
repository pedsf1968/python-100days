from turtle import Turtle
import parameters as p


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(p.BALL_COLOR)
        self.penup()
        self.x_move = p.BALL_MOVE
        self.y_move = p.BALL_MOVE
        self.move_speed = 0.1

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)
        print(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        self.x_move += 1
        self.y_move += 1
