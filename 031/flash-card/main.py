from tkinter import *
import pandas
import random

FLASHY_BACKGROUND_COLOR = "#B1DDC6"
FLASHY_FRONT_IMAGE = "./images/card_front.png"
FLASHY_FRONT_FG = "black"
FLASHY_BACK_IMAGE = "./images/card_back.png"
FLASHY_BACK_FG = "white"
FLASHY_RIGHT_LOGO = "./images/right.png"
FLASHY_WRONG_LOGO = "./images/wrong.png"
FLASHY_LANGUAGE_FILE = "./data/korean-french-1000.csv"
FLASHY_TO_LEARN_FILE = "./data/korean-french-to-learn.csv"
FLASHY_TIMER = 3000

FLASHY_LANGUAGE_FONT_NAME = "Ariel"
FLASHY_LANGUAGE_FONT_SIZE = 40
FLASHY_LANGUAGE_FONT_TYPE = "italic"
FLASHY_WORD_FONT_NAME = "Ariel"
FLASHY_WORD_FONT_SIZE = 60
FLASHY_WORD_FONT_TYPE = "bold"

flip_timer = None
flashy_data = {}
current_card = {}


def load_dictionary(filename):
    global flashy_data
    data = None
    try:
        # Default load only the dictionary to learn
        data = pandas.read_csv(FLASHY_TO_LEARN_FILE)
    except FileNotFoundError:
        # If no dictionary is present, load all words
        data = pandas.read_csv(FLASHY_LANGUAGE_FILE)
    finally:
        flashy_data = data.to_dict(orient="records")


def pick_a_card():
    global flashy_data
    return random.choice(flashy_data)


def next_card():
    global current_card, flip_timer
    try:
        window.after_cancel(flip_timer)
    except:
        pass
    current_card = pick_a_card()
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(label_language, text="Korean", fill=FLASHY_FRONT_FG)
    canvas.itemconfig(label_word, text=current_card["Korean"], fill=FLASHY_FRONT_FG)
    flip_timer = window.after(FLASHY_TIMER, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(label_language, text="French", fill=FLASHY_BACK_FG)
    canvas.itemconfig(label_word, text=current_card["French"], fill=FLASHY_BACK_FG)
    canvas.grid(row=0, column=0, columnspan=2)


def known_word():
    try:
        flashy_data.remove(current_card)
    except ValueError:
        pass
    finally:
        df = pandas.DataFrame(flashy_data)
        df.to_csv(FLASHY_TO_LEARN_FILE, index=False)
        next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=FLASHY_BACKGROUND_COLOR)


canvas = Canvas(width=800,height=526, bg=FLASHY_BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file=FLASHY_FRONT_IMAGE)
back_image = PhotoImage(file=FLASHY_BACK_IMAGE)
canvas_image = canvas.create_image(400, 263, image=front_image)
#canvas_back_image = canvas.create_image(400, 263, image=back_image)


label_language = canvas.create_text(400, 150, text="",
                                    font=(FLASHY_LANGUAGE_FONT_NAME, FLASHY_LANGUAGE_FONT_SIZE, FLASHY_LANGUAGE_FONT_TYPE))
label_word = canvas.create_text(400, 253, text="",
                                font=(FLASHY_WORD_FONT_NAME, FLASHY_WORD_FONT_SIZE, FLASHY_WORD_FONT_TYPE))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file=FLASHY_RIGHT_LOGO)
wrong_image = PhotoImage(file=FLASHY_WRONG_LOGO)
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=known_word)
wrong_button.grid(row=1, column=1)

load_dictionary(FLASHY_LANGUAGE_FILE)
next_card()
window.mainloop()