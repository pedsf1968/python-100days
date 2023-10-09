from turtle import Turtle, Screen
import random


class MyTurtle:

    def __init__(self, color, x_position, y_position):
        self.turtle = Turtle(shape="turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.turtle.goto(x_position, y_position)

    def move(self):
        self.x_position += random.randint(0, 10)
        self.turtle.goto(self.x_position, self.y_position)


screen = Screen()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
NUMBER_OD_TURTLES = 6
colors = ["red", "orange", "yellow", "green", "blue", "purple", "gray", "black", "cyan", "turquoise", "teal", "lime",
          "beige", "olive", "khaki", "gold", "tan", "lavender", "indigo", "violet", "magenta", "pink", "salmon", "tomato"]


def turtle_create(number=NUMBER_OD_TURTLES):
    turtles = []
    spaces = int(SCREEN_HEIGHT/(NUMBER_OD_TURTLES+1))
    position = spaces - SCREEN_HEIGHT/2
    for index in range(0, number):
        new_turtle = MyTurtle(colors[index], x_position=20-SCREEN_WIDTH/2, y_position=position)
        position += spaces
        turtles.append(new_turtle)
    return turtles


def main():
    is_race_on = False
    user_bet = ""
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    while user_bet not in colors:
        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        is_race_on = True

    all_turtle = turtle_create(number=NUMBER_OD_TURTLES)

    while is_race_on:
        for turtle in all_turtle:
            turtle.move()
            if turtle.x_position > SCREEN_WIDTH/2-20:
                is_race_on = False
                winning_color = turtle.color
                if user_bet == winning_color:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

    screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()