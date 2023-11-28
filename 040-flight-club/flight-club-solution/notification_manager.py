import smtplib
from twilio.rest import Client
from os import environ

TWILIO_SID = environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = environ['TWILIO_AUTH_TOKEN']
TWILIO_VIRTUAL_NUMBER = environ['TWILIO_PHONE_NUMBER']
TWILIO_VERIFIED_NUMBER = environ['TWILIO_PHONE_NUMBER']
MAIL_PROVIDER_SMTP_ADDRESS = environ["SMTPLIB_SMTP_SERVER"]
MY_EMAIL = environ["SMTPLIB_EMAIL"]
MY_PASSWORD = environ["SMTPLIB_PASSWORD"]

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )