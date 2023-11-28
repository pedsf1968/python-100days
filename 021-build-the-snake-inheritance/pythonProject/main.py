from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import parameters as p
import time


def main():
    # Create the screen
    screen = Screen()
    screen.bgcolor(p.SCREEN_COLOR)
    screen.setup(width=p.SCREEN_WIDTH, height=p.SCREEN_HEIGHT)
    screen.title(p.SCREEN_TITLE)
    screen.tracer(0)
    screen.listen()

    # Create and move a paddle
    left_paddle = Paddle(-p.SCREEN_WITH_RANGE)
    screen.onkey(left_paddle.up, "a")
    screen.onkey(left_paddle.down, "q")
    # Create another paddle
    right_paddle = Paddle(p.SCREEN_WITH_RANGE-10)
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")

    # Create the ball and make it move
    ball = Ball()
    # Keep score
    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        # Detect collision with wall and bounce
        if ball.ycor() < -280 or ball.ycor() > 280:
            ball.bounce_y()
        # Detect collision with right paddle
        if ball.distance(right_paddle) < 50 and ball.xcor() > 340 \
                or ball.distance(left_paddle) < 50 and ball.xcor() < -350:
            ball.bounce_x()

        # Detect when paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.increase("LEFT")

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.increase("RIGHT")
            #game_is_on = False

    screen.exitonclick()


if __name__ == '__main__':
    main()

