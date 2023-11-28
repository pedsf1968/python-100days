from tkinter import *
from tkinter import messagebox
import pyperclip, json
from password_generator import password_create

PWM_LOGO_FILE = "logo.png"
PWM_BACKUP_FILE = "pwm_data.json"
PWM_PASSWORD_LENGTH = 12
PWM_DEFAULT_LOGIN = ""
COLUMN_SINGLE_WIDE = 25
COLUMN_DOUBLE_WIDE = 50

PWM_WARNING_TITLE = "Warning"
PWM_WARNING_MATCH = "Password and confirmation doesn't match!"
PWM_WARNING_WEBSITE = "You must specify a website!"
PWM_WARNING_LOGIN = "You must specify a login!"
PWM_WARNING_PASSWORD = "You must specify a password!"
PWM_WARNING_FILE_NOT_FOUND = "Recorded datas not found!"
PWM_WARNING_WEBSITE_NOT_FOUND = "Website not found!"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def reset_window():
    website_entry.delete(0,END)
    login_entry.delete(0,END)
    login_entry.insert(0, PWM_DEFAULT_LOGIN)
    password_entry.delete(0,END)
    password_confirmation_entry.delete(0, END)


def generate_password():
    passwrd = password_create(length=PWM_PASSWORD_LENGTH)
    password_entry.delete(0,END)
    password_confirmation_entry.delete(0,END)
    password_entry.insert(END, passwrd)
    password_confirmation_entry.insert(END, passwrd)
    pyperclip.copy(passwrd)


def save_credentials():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()

    confirmation = password_confirmation_entry.get()
    if confirmation != password:
        messagebox.showwarning(title=PWM_WARNING_TITLE, message=PWM_WARNING_MATCH)
    elif website == "":
        messagebox.showwarning(title=PWM_WARNING_TITLE, message=PWM_WARNING_WEBSITE)
    elif login == "":
        messagebox.showwarning(title=PWM_WARNING_TITLE, message=PWM_WARNING_LOGIN)
    elif password == "":
        messagebox.showwarning(title=PWM_WARNING_TITLE, message=PWM_WARNING_PASSWORD)
    else:
        new_data = {
            website: {
                "login": login,
                "password": password,
            }
        }
        try:
            with open(PWM_BACKUP_FILE, "r") as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError:
            with open(PWM_BACKUP_FILE, "w") as json_file:
                json.dump(new_data, json_file, indent=4)
        else:
            json_data.update(new_data)
            with open(PWM_BACKUP_FILE, "w") as json_file:
                json.dump(json_data, json_file, indent=4)
        finally:
            reset_window()


def search_credentials():
    website = website_entry.get()
    try:
        with open(PWM_BACKUP_FILE, "r") as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        messagebox.showwarning(title=PWM_WARNING_TITLE, message=PWM_WARNING_FILE_NOT_FOUND)
    else:
        if website in json_data:
            login = json_data[website]["login"]
            password = json_data[website]["password"]
            messagebox.showinfo(title=website, message=f"Login: {login}\nPassword: {password}")
        else:
            messagebox.showwarning(title=PWM_WARNING_TITLE, message=PWM_WARNING_WEBSITE_NOT_FOUND)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_image = PhotoImage(file=PWM_LOGO_FILE)
canvas = Canvas(width=200,height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
login_label = Label(text="Email/Username:")
login_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_confirmation_label = Label(text="Confirmation:")
password_confirmation_label.grid(row=4, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
login_entry = Entry(width=50)
login_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=30, show="*")
password_entry.grid(row=3, column=1)
password_confirmation_entry = Entry(width=30, show="*")
password_confirmation_entry.grid(row=4, column=1)

search_button = Button(text="Search", width=14, command=search_credentials)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_credentials_button = Button(text="Add Credentials", width=14, command=save_credentials)
add_credentials_button.grid(row=4, column=2)

reset_window()

window.mainloop()