import smtplib
from datetime import datetime
import pandas
from random import randint

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

today = datetime.now().month
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["mday"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = "letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



