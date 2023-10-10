from turtle import Turtle
import parameters as p


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.color(p.PLAYER_COLOR)
        self.setheading(90)
        self.penup()
        self.goto(p.PLAYER_POSITION)

    def up(self):
        self.forward(p.PLAYER_MOVE)

    def reset_position(self):
        self.goto(p.PLAYER_POSITION)
