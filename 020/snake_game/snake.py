from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_COLOR = "white"
SNAKE_UP = 90
SNAKE_DOWN = 270
SNAKE_LEFT = 180
SNAKE_RIGHT = 0
MOVE_DISTANCE = 20



class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color(SNAKE_COLOR)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != SNAKE_DOWN:
            self.head.setheading(SNAKE_UP)

    def down(self):
        if self.head.heading() != SNAKE_UP:
            self.head.setheading(SNAKE_DOWN)

    def left(self):
        if self.head.heading() != SNAKE_RIGHT:
            self.head.setheading(SNAKE_LEFT)

    def right(self):
        if self.head.heading() != SNAKE_LEFT:
            self.head.setheading(SNAKE_RIGHT)
