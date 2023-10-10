import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()


def main():
    screen.setup(width=600, height=600)
    screen.title("My Turtle Crossing")
    screen.tracer(0)

    player = Player()
    screen.onkey(player.up, "Up")
    screen.listen()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

    if player.ycor() > 300:
        print("cross")
    screen.exitonclick()


if __name__ == '__main__':
    main()
