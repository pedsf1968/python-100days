# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# https://openweathermap.org/api/one-call-3
# https://www.ventusky.com/
import requests
import os
from twilio.rest import Client

TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
# MY_LATITUDE = 47.241270
# MY_LONGITUDE = 6.025530
MY_LATITUDE = 48.52
MY_LONGITUDE = 1.13

OPENWEATHERMAP_ONECALLAPI_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
OPENWEATHERMAP_API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")


def get_weather(exclude="hourly", hour_max=6):
    exclude_data = ["current", "minutely", "hourly", "daily", "alerts"]
    exclude_data.remove(exclude)
    request_params = {
        "lat": MY_LATITUDE,
        "lon": MY_LONGITUDE,
        "appid": OPENWEATHERMAP_API_KEY,
        "exclude": ",".join(exclude_data),
        "units": "metric",
    }
    print(request_params)
    response = requests.get(url=OPENWEATHERMAP_ONECALLAPI_ENDPOINT, params=request_params)
    response.raise_for_status()
    weather_data = response.json()
    print(weather_data)
    weather_slice = weather_data[exclude][:hour_max]
    print(weather_slice)
    return weather_slice


def need_umbrella(weather_data):
    will_rain = False
    for hour_data in weather_data:
        weather_id = int(hour_data["weather"][0]["id"])
        if weather_id < 700:
            will_rain = True
    return will_rain


def send_message(phone_to: str, message: str, phone_from=TWILIO_PHONE_NUMBER):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    print(auth_token, account_sid)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=phone_from,
        to=phone_to
    )
    print(message.status)


def main():
    weather_data = get_weather(exclude="hourly", hour_max=12)
    if need_umbrella(weather_data=weather_data):
        send_message(phone_to="+33783752124", message="It's going to rain today. Remember to bring an ☂️")


if __name__ == "__main__":
    main()