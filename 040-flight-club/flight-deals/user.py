import requests
from os import environ


def ask_something(message):
    something = input(message)
    if something == "":
        return ask_something(message)
    else:
        return something


def ask_something_with_confirmation(message1, message2):
    something = ask_something(message1)
    confirmation = ask_something(message2)
    if something != confirmation:
        ask_something_with_confirmation(message1, message2)
    else:
        return something


class User:
    def __init__(self, first_name="", last_name="", email=""):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def display(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")

    def ask(self):
        self.first_name = ask_something("What's your first name? ")
        self.last_name = ask_something("What's your last name? ")
        self.email = ask_something_with_confirmation("What's your email? ","Type your email? ")

    def register(self):
        endpoint = environ.get("SHEETY_FLIGHTDEALS_URL") + "/users"
        token = environ.get("SHEETY_FLIGHTDEALS_TOKEN")

        header = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        body = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }
        response = requests.post(url=endpoint, headers=header, json=body)
        response.raise_for_status()
        print(response.text)
        print("You're in the club!")
