import requests
from os import environ
from user import User


class Users:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        new_user = User(first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email)
        self.users.append(new_user)

    def get_users(self):
        endpoint = environ.get("SHEETY_FLIGHTDEALS_URL") + "/users"
        token = environ.get("SHEETY_FLIGHTDEALS_TOKEN")
        header = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        response = requests.get(url=endpoint, headers=header)
        data = response.json()["users"]
        for item in data:
            new_user = User(first_name=item["firstName"],
                            last_name=item["lastName"],
                            email=item["email"])
            self.users.append(new_user)
        return self.users

    def display(self):
        for user in self.users:
            user.display()
