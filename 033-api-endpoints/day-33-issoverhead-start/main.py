# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# // 20231019163128
# // http://api.open-notify.org/iss-now.json
#
# {
#   "timestamp": 1697725888,
#   "message": "success",
#   "iss_position": {
#     "latitude": "-43.4752",
#     "longitude": "55.2452"
#   }
# }
# https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh
import requests


def main():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # For HTTP error raise exception
    response.raise_for_status()
    # Get data in JSON
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    iss_position = (longitude, latitude)
    print(iss_position)


if __name__ == '__main__':
    main()

