import smtplib
import datetime as dt
import random

BW_EMAIL = "pedsf.fullstack@gmail.com"
BW_PASSWORD = "######"
BW_SMTP_SERVER = "smtp.gmail.com"
BW_QUOTES_FILE = "quotes.txt"
BW_TUESDAY = 2


def read_quote():
    with open(BW_QUOTES_FILE) as data:
        data = data.readlines()
    return random.choice(data)


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
    now = dt.datetime.now()
    print(now.weekday())
    if now.weekday() == BW_TUESDAY:
        quote = read_quote()
        send_mail(BW_EMAIL, subject="Mail of the day", content=quote)
    else:
        print("Not Tuesday")


if __name__ == "__main__":
    main()