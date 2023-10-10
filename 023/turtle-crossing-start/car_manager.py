from turtle import Turtle
import random
import parameters as p


class CarManager:

    def __init__(self):
        self.cars = []
        self.dice_faces = p.CAR_DICE_FACES
        self.car_speed = p.CAR_STARTING_MOVE_DISTANCE

    def add_car(self):
        if random.randint(1, self.dice_faces) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=p.CAR_STRETCH_WIDTH, stretch_len=p.CAR_STRETCH_LENGTH)
            new_car.color(random.choice(p.CAR_COLORS))
            new_car.setheading(180)
            new_car.penup()
            x_pos = p.CAR_X_RANGE
            y_pos = random.randint(-p.CAR_Y_RANGE, p.CAR_Y_RANGE)
            new_car.goto(x_pos, y_pos)
            self.cars.append(new_car)

    def move(self, player):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.distance(player) < 10:
                return False
            if car.xcor() < -p.SCREEN_WITH_RANGE:
                x_pos = p.SCREEN_WITH_RANGE
                y_pos = random.randint(-p.CAR_Y_RANGE, p.CAR_Y_RANGE)
                car.goto(x_pos, y_pos)
        return True

    def level_up(self):
        self.car_speed += p.CAR_MOVE_INCREMENT


