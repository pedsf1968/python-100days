import pandas
import turtle

DATA_FILE = "50_states.csv"
IMAGE_FILE = "blank_states_img.gif"
SCREEN_TITLE = "U.S. States Game"
RESULT_FILE = "states_to_learn.csv"


def write_state(data, state_name):
    state_data = data[data.state == state_name]
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
    #state.write(state_data.state.item())
    state.write(state_name)


def save_not_found(all_data, found_data):
    for item in found_data:
        all_data.remove(item)
    dataframe = pandas.DataFrame(all_data)
    dataframe.to_csv(RESULT_FILE)


def main():
    screen = turtle.Screen()
    screen.title(SCREEN_TITLE)
    screen.addshape(IMAGE_FILE)
    turtle.shape(IMAGE_FILE)
    data = pandas.read_csv(DATA_FILE)
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            save_not_found(all_states, guessed_states)
            break

        # Check if the state exist
        if answer_state in all_states:
            write_state(data, answer_state)
            guessed_states.append(answer_state)
        else:
            print(f"Error state {answer_state}")


if __name__ == "__main__":
    main()