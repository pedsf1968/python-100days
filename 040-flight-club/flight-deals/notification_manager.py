# https://www.twilio.com/docs/sms
from twilio.rest import Client
import smtplib
from os import environ


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        # For SMS
        self.account_sid = environ['TWILIO_ACCOUNT_SID']
        self.auth_token = environ['TWILIO_AUTH_TOKEN']
        self.phone_from = environ['TWILIO_PHONE_NUMBER']
        self.client = Client(self.account_sid, self.auth_token)
        # For emails
        self.smtp_server = environ["SMTPLIB_SMTP_SERVER"]
        self.smtp_email = environ["SMTPLIB_EMAIL"]
        self.smtp_password = environ["SMTPLIB_PASSWORD"]

    def send_message(self, phone_to, message):
        message = self.client.messages.create(
            body=message,
            from_=self.phone_from,
            to=phone_to
        )
        print(message.sid)

    def send_emails(self, destinations, subject, content):
        with smtplib.SMTP(self.smtp_server) as connection:
            # Secure the connection
            connection.starttls()
            connection.login(user=self.smtp_email, password=self.smtp_password)
            for destination in destinations:
                connection.sendmail(
                    from_addr=self.smtp_email,
                    to_addrs=destination,
                    msg=f"Subject:{subject}\n\n{content.encode('utf-8')}")

