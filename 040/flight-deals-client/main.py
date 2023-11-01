import requests
from os import environ
from user import User


def main():
    user = User()
    # user.ask()
    # user.register()
    users = user.get_users()
    for user in users:
        print(user)



if __name__ == "__main__":
    main()

