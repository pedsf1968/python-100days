# Check if we can see ISS
import requests
from datetime import datetime
import smtplib
import time

SUNSET_SUNRISE_API = "https://api.sunrise-sunset.org/json"
ISS_OPEN_NOTIFY_API = "http://api.open-notify.org/iss-now.json"
MY_LATITUDE = 47.241270
MY_LONGITUDE = 6.025530
MY_EMAIL = "pedsf.fullstack@gmail.com"
MY_PASSWORD = "###########"
MY_SMTP_SERVER = "smtp.gmail.com"


def is_iss_overhead():
    response = requests.get(url=ISS_OPEN_NOTIFY_API)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    print(f"Latitude: {MY_LATITUDE - 5} <= {iss_latitude} <= {MY_LATITUDE + 5}")
    print(f"Longitude: {MY_LONGITUDE - 5} <= {iss_longitude} <= {MY_LONGITUDE + 5}:")
    if MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get(SUNSET_SUNRISE_API, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.now().hour
    print(f"Sunrise: {sunrise}, now: {now}, Sunset: {sunset}")
    if now < sunrise or now > sunset:
        return True
    else:
        return False


def send_mail():
    with smtplib.SMTP(MY_SMTP_SERVER) as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:ISS overhead\n\nIt's time to see the ISS in the sky!"
        )


def main():
    while True:
        if is_iss_overhead() and is_night():
            send_mail()
        time.sleep(60)


if __name__ =="__main__":
    main()

