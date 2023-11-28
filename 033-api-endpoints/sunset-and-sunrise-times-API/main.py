# https://sunrise-sunset.org/api
# Parameters
# lat (float): Latitude in decimal degrees. Required.
# lng (float): Longitude in decimal degrees. Required.
# date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. If not present, date defaults to current date. Optional.
# callback (string): Callback function name for JSONP response. Optional.
# formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.
import requests
from datetime import datetime


SUNSET_SUNRISE_API_URL = "https://api.sunrise-sunset.org/json"
# MY_LATITUDE = 37.572891
# MY_LONGITUDE = 126.977118
MY_LATITUDE = 47.241270
MY_LONGITUDE = 6.025530

def query_sunset(parameters):
    response = requests.get(url=SUNSET_SUNRISE_API_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    # Get only hour
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    return (sunrise,sunset)


def querry_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # For HTTP error raise exception
    response.raise_for_status()
    # Get data in JSON
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    return (longitude, latitude)


def main():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    iss_position = querry_iss_position()
    print(iss_position)
    print(query_sunset(parameters))
    print(datetime.now().hour)



if __name__ =="__main__":
    main()