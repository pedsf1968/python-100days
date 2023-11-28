from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


def main():
    game_is_on = True
    snake = Snake()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    while game_is_on:
        screen.update()
        time.sleep(1)
        snake.move()

    screen.exitonclick()


if __name__ == '__main__':
    main()