from turtle import Turtle
import random
import parameters as p


class CarManager:

    def __init__(self):
        self.cars = []
        self.add_car()

    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(p.CAR_COLORS))
        new_car.setheading(180)
        new_car.penup()
        x_pos = p.SCREEN_WITH_RANGE
        y_pos = random.randint(-p.CAR_Y_RANGE, p.CAR_Y_RANGE)
        new_car.goto(x_pos, y_pos)
        self.cars.append(new_car)

    def move(self, player):
        for car in self.cars:
            car.forward(random.randint(0, 20))
            if car.distance(player) < 5:
                return False
            if car.xcor() < -p.SCREEN_WITH_RANGE:
                x_pos = p.SCREEN_WITH_RANGE
                y_pos = random.randint(-p.CAR_Y_RANGE, p.CAR_Y_RANGE)
                car.goto(x_pos, y_pos)
        return True




