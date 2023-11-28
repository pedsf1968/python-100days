# https://www.twilio.com/docs/sms
from twilio.rest import Client
from os import environ


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = environ['TWILIO_ACCOUNT_SID']
        self.auth_token = environ['TWILIO_AUTH_TOKEN']
        self.phone_from = environ['TWILIO_PHONE_NUMBER']
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, phone_to, message):
        message = self.client.messages.create(
            body=message,
            from_=self.phone_from,
            to=phone_to
        )
        print(message.sid)