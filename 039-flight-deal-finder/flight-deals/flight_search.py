# https://partners.kiwi.com/
# https://tequila.kiwi.com/portal/docs/tequila_api
from os import environ
import requests
import datetime
from pprint import pprint
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_FLY_FROM = "CDG"
TEQUILA_DATE_FROM = datetime.datetime.now() + datetime.timedelta(days=1)
TEQUILA_DATE_TO = datetime.datetime.now() + datetime.timedelta(days=180)
TEQUILA_DESTINATION_NIGHTS_MIN = 7
TEQUILA_DESTINATION_NIGHTS_MAX = 28
TEQUILA_MAX_STOPOVERS = 1
TEQUILA_CURRENCY = "EUR"
TEQUILA_LOCALE = "fr"

selected_cabins = {
    "economy": "M",
    "premium": "W",
    "business": "C",
    "first": "F"
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = TEQUILA_ENDPOINT
        self.apikey = environ.get("TEQUILA_API_KEY")

    def get_iatacode(self, city):
        """Return IATA code for specified city
            city : the city name
        """
        url = self.url + "/locations/query"
        header = {"apikey": self.apikey}
        body = {
            "term": city,
            "locale": "fr-FR",
            "location_types": "city",
            "limit": 1,
            "active_only": "true"
        }
        response = requests.get(url=url, headers=header, params=body)
        return response.json()["locations"][0]["code"]

    def search(self, fly_to,
               fly_from=TEQUILA_FLY_FROM,
               date_from=TEQUILA_DATE_FROM.strftime("%d/%m/%Y"),
               date_to=TEQUILA_DATE_TO.strftime("%d/%m/%Y")):
        """Search lower price fly from TEQUILA_FLY_FROM to specified destination
            fly_to : IATA destination code
            fly_from : IATA departure code, default TEQUILA_FLY_FROM
            date_from : search starting date, default TEQUILA_DATE_FROM
            date_to : search ending date, default TEQUILA_DATE_TO
        """
        url = self.url + "/v2/search"
        header = {"apikey": self.apikey}
        body = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": TEQUILA_DESTINATION_NIGHTS_MIN,
            "nights_in_dst_to": TEQUILA_DESTINATION_NIGHTS_MAX,
            "selected_cabins": selected_cabins["economy"],
            # "flight_type": "round",
            # "one_for_city": 1,
            "max_stopovers": TEQUILA_MAX_STOPOVERS,
            "adult_hold_bag": 1,
            "adult_hand_bag": 1,
            "curr": TEQUILA_CURRENCY,
            "locale": TEQUILA_LOCALE,
        }
        response = requests.get(url=url, headers=header, params=body)
        try:
            data = response.json()["data"]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None

        lowest_price = data[0]["conversion"][TEQUILA_CURRENCY]
        flight_data = ""
        for fly in data:
            curent_price = fly["conversion"][TEQUILA_CURRENCY]
            if curent_price <= lowest_price :
                flight_data = FlightData(fly)
                lowest_price = curent_price
                flight_data.display()
        return flight_data
