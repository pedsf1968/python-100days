from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from properties import *

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

def main():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < FOOD_COLLISION_MARGIN:
            food.refresh()
            snake.extend()
            scoreboard.increase()

        # detect collision with wall
        if snake.head.xcor() > SCREEN_WITH_RANGE \
                or snake.head.xcor() < -SCREEN_WITH_RANGE \
                or snake.head.ycor() > SCREEN_HEIGHT_RANGE \
                or snake.head.ycor() < -SCREEN_HEIGHT_RANGE:
            scoreboard.reset()
            snake.reset()

        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < SEGMENT_COLLISION_MARGIN:
                scoreboard.reset()
                snake.reset()

    screen.exitonclick()


if __name__ == '__main__':
    main()
