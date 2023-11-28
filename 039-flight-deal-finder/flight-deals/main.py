#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from os import environ

MY_PHONE = environ.get("MY_PHONE")


def main():
    data_manager = DataManager()
    data_manager.get()
    data_manager.update_iatacode()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    for destination in data_manager.data:
        flight_data = flight_search.search(fly_to=destination["iataCode"])
        if flight_data.price <= destination["lowestPrice"]:
            notification_manager.send_message(phone_to=MY_PHONE, message=flight_data.build_message())
            destination["lowestPrice"] = flight_data.price
            data_manager.update_price()
            flight_data.display()

    # flight_data = flight_search.search(fly_from="DLE", fly_to="OPO")
    # flight_data.display()
    # if flight_data.price <= 1000:
    #     notification_manager.send_message(phone_to=MY_PHONE, message=flight_data.build_message())


if __name__ == "__main__":
    main()