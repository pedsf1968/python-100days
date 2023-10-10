import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import parameters as p

screen = Screen()


def main():
    scoreboard = Scoreboard()
    player = Player()
    car_manager = CarManager()
    screen.setup(width=p.SCREEN_WIDTH, height=p.SCREEN_HEIGHT)
    screen.title(p.SCREEN_TITLE)
    screen.tracer(0)
    screen.onkey(player.up, "Up")
    screen.listen()

    game_is_on = True
    counter = 6
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        game_is_on = car_manager.move(player)
        counter -= 1
        if counter == 0:
            counter = 6
            car_manager.add_car()

        if player.ycor() > p.SCREEN_HEIGHT_RANGE:
            scoreboard.increase_score()
            player.reset_position()

    scoreboard.game_over()

if __name__ == '__main__':
    main()
    screen.exitonclick()
