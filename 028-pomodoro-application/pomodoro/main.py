# https://colorhunt.co/
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE = 35
FONT_TYPE = "bold"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def button_reset_action():
    global reps
    global timer
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_checkmarks.config(text="")


def button_start_action():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label_timer.config(text="Work", fg=GREEN)


    # ---------------------------- TIMER MECHANISM ------------------------------- #

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        button_start_action()
        checks_marks = ""
        # Add checkmark every 2 reps
        for _ in range(math.floor(reps/2)):
            checks_marks += "✔"
        label_checkmarks.config(text=checks_marks)

    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label_timer.grid(row=0, column=1)

# Load tomato picture
photo_tomato = PhotoImage(file="tomato.png")
# highlightthickness=0 remove border
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo_tomato)
# Add timer
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, FONT_TYPE))
# Change color bg
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=button_start_action, highlightthickness=0)
button_start.grid(row=2, column=0)
button_reset = Button(text="Reset", command=button_reset_action, highlightthickness=0)
button_reset.grid(row=2, column=2)

label_checkmarks = Label(fg=GREEN, bg=YELLOW)
label_checkmarks.grid(row=3, column=1)

window.mainloop()
