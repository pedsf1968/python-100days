from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_MARGIN = 20
SCREEN_WITH_RANGE = int(SCREEN_WIDTH/2) - SCREEN_MARGIN
SCREEN_HEIGHT_RANGE = int(SCREEN_HEIGHT/2) - SCREEN_MARGIN
FOOD_COLLISION_MARGIN = 15
SEGMENT_COLLISION_MARGIN = 10

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
            scoreboard.game_over()
            game_is_on = False

        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < SEGMENT_COLLISION_MARGIN:
                scoreboard.game_over()
                game_is_on = False

    screen.exitonclick()


if __name__ == '__main__':
    main()
