from tkinter import *


def convert():
    kilometer = round(float(entry_miles.get()) * 1.60934,2)
    label_result.config(text=f"is equal {kilometer} to km")

windows = Tk()
windows.title("Mile to KM Converter")
windows.minsize(width=300, height=150)
windows.config(padx=20, pady=20)

# Add entry
entry_miles = Entry()
entry_miles.grid(row=0, column=1)
entry_miles.focus()
label_miles = Label(text="Miles", font=("Arial", 12, "normal"))
label_miles.grid(row=0, column=2)

label_result = Label(text="Enter a distance in miles", font=("Arial", 12, "normal"))
label_result.grid(row=1, column=1)

button_calculate = Button(text="Calculate", command=convert)
button_calculate.grid(row=2, column=1)


windows.mainloop()
