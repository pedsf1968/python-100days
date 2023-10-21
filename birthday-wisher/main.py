# PEDSF
# DATE : 2023/10/18
import datetime as dt
import pandas
import os
import smtplib
import random

BW_EMAIL = "pedsf.fullstack@gmail.com"
BW_PASSWORD = "###########"
BW_SMTP_SERVER = "smtp.gmail.com"
BW_QUOTES_FILE = "quotes.txt"
BW_TUESDAY = 2
BW_LETTER_TEMPLATES_FOLDER = "./letter_templates"
BW_BIRTHDAYS_FILE = "./birthdays.csv"

today_birthday = []


def search_today_birthdays():
    global today_birthday
    data = pandas.read_csv(BW_BIRTHDAYS_FILE)
    birth_data = data.to_dict(orient="records")
    now = dt.datetime.now()
    now_month = now.month
    now_day = now.day
    for item in birth_data:
        if item["month"] == now_month and item["day"] == now_day:
            today_birthday.append(item)


def pick_letter(folder):
    files = []
    for file_path in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file_path)):
            files.append(os.path.join(folder, file_path))
    return random.choice(files)


def replace_word_in_letter(file_path, word):
    with open(file_path) as file:
        content = file.read()
        new_letter = content.replace("[NAME]", word)
    return new_letter


def send_mail(destination, subject, content):
    with smtplib.SMTP(BW_SMTP_SERVER) as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=BW_EMAIL, password=BW_PASSWORD)
        connection.sendmail(
            from_addr=BW_EMAIL,
            to_addrs=destination,
            msg=f"Subject:{subject}\n\n{content}"
        )


def main():
    search_today_birthdays()
    for item in today_birthday:
        letter_name = pick_letter(BW_LETTER_TEMPLATES_FOLDER)
        letter_content = replace_word_in_letter(letter_name, item["name"])
        send_mail(item["email"], subject="Happy Birthday!", content=letter_content)


if __name__ == "__main__":
    main()


