# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from users import Users
from user import User
from notification_manager import NotificationManager
from os import environ

MY_PHONE = environ.get("MY_PHONE")


def main():
    data_manager = DataManager()
    data_manager.get()
    data_manager.update_iatacode()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    # Get all users
    users = Users()
    data = users.get_users()
    mailing_list = [item.email for item in data]

    for destination in data_manager.data:
        flight_data = flight_search.search(fly_to=destination["iataCode"])
        if flight_data is None:
            continue
        if flight_data.price <= destination["lowestPrice"]:
            print("Lower price!")
            # notification_manager.send_message(phone_to=MY_PHONE,
            #                                   message=flight_data.build_message())
            notification_manager.send_emails(destinations=mailing_list,
                                             subject="Fly discount",
                                             content=flight_data.build_message())

      # flight_data = flight_search.search(fly_to="DPS")
    # flight_data.display()
    # if flight_data.price <= 1000:
    #     notification_manager.send_message(phone_to=MY_PHONE, message=flight_data.build_message())


if __name__ == "__main__":
    main()