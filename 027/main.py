from tkinter import *


def button_clicked():
    print("You click the button:")
    new_text = input.get()
    my_label.config(text=new_text)


# Create a windows
windows = Tk()
windows.title("My first usage of GUI ")
# Set default windows size
windows.minsize(width=500, height=300)

# Add label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# Place the label in the center of the screen
# my_label.pack(side="left")
my_label.pack(side="top")
# my_label.pack(side="right")
# my_label.pack(side="top")
# my_label.pack(expand=True)
my_label["text"] = "New text"
my_label.config(text="Another label")

# Add button
button = Button(text="Click Here", command=button_clicked)
button.pack(side="top")


# Add input
input = Entry()
input.pack(side="top")
print(input)

# Loop to listen user action
windows.mainloop()
