# https://sheety.co/
from os import environ
import requests
from pprint import pprint


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = environ.get("SHEETY_FLIGHTDEALS_URL") + "/prices"
        self.token = environ.get("SHEETY_FLIGHTDEALS_TOKEN")
        self.data = {}
        self.get()

    def display(self):
        pprint(self.data)

    def get(self):
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=self.endpoint, headers=header)
        if response.status_code == 200:
            self.data = response.json()["prices"]

    def update_iatacode(self):
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        for destination in self.data:
            from flight_search import FlightSearch
            flight_search = FlightSearch()
            if destination["iataCode"] == "":
                destination["iataCode"] = flight_search.get_iatacode(destination["city"])
                body = {
                    "price": {
                        "iataCode": destination["iataCode"]
                    }
                }
                response = requests.put(url=f"{self.endpoint}/{destination['id']}", headers=header, json=body)
                print(response.text)

    def update_price(self):
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        for destination in self.data:
            from flight_search import FlightSearch
            flight_search = FlightSearch()
            body = {
                "price": {
                    "lowestPrice": destination["lowestPrice"]
                }
            }
            response = requests.put(url=f"{self.endpoint}/{destination['id']}", headers=header, json=body)
            print(response.text)
