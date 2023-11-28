# https://docs.pixe.la/
# https://pixe.la/
# https://requests.readthedocs.io/en/latest/api/
import requests
from os import environ
import datetime

HT_PIXELA_USERNAME = environ.get("PIXELA_USERNAME")
HT_PIXELA_TOKEN = environ.get("PIXELA_TOKEN")
HT_PIXELA_ENDPOINT = "https://pixe.la/"
HT_GRAPH_ID = "pedsfgraph1"


def pixela_user_create(username, token):
    """Create a user with a specified token
        username: the name of the user
        token: the token to use"""
    endpoint = f"{HT_PIXELA_ENDPOINT}v1/users"
    data = {
        "username": username,
        "token": token,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=endpoint, json=data)
    print(response.text)


def pixela_graph_create(username, token, graph_id, graph_name, graph_unit="km", graph_type="float", graph_color="ajisai"):
    """Create a graph for a specified user
        username: the name of the user 
        token: the token to identify the user
        graph_id: the graph identifier
        graph_name: the name to display in the graph
        graph_unit: the graph unit (default "km")
        graph_type: the data type (default "float")
        graph_color: the graph color (default "ajisai)
    """
    endpoint = f"{HT_PIXELA_ENDPOINT}v1/users/{username}/graphs"
    header = {
        "X-USER-TOKEN": token
    }
    data = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": graph_type,
        "color": graph_color,
    }
    response = requests.post(url=endpoint, headers=header, json=data)
    print(response.text)


def pixela_pixel_create(username, token, graph_id, data_quantity, data_date=datetime.date.today().strftime('%Y%m%d')):
    """Add data to a specified graph today
        username: the name of the user
        token: the token to identify the user
        graph_id: the graph identifier
        data_quantity: the quantity to add
        data_date: the date to insert data default is now
    """
    endpoint = f"{HT_PIXELA_ENDPOINT}v1/users/{username}/graphs/{graph_id}"
    header = {
        "X-USER-TOKEN": token
    }
    data = {
        "date": data_date,
        "quantity": data_quantity,
    }
    response = requests.post(url=endpoint, headers=header, json=data)
    print(response.text)


def pixela_pixel_create_asking(username, token, graph_id):
    """Add data to a specified graph today
        username: the name of the user
        token: the token to identify the user
        graph_id: the graph identifier
        data_quantity: the quantity to add
        data_date: the date to insert data default is now
    """
    endpoint = f"{HT_PIXELA_ENDPOINT}v1/users/{username}/graphs/{graph_id}"
    header = {
        "X-USER-TOKEN": token
    }
    data = {
        "date":  datetime.date.today().strftime('%Y%m%d'),
        "quantity": input("How many kilometers did you cycle today? "),
    }
    response = requests.post(url=endpoint, headers=header, json=data)
    print(response.text)


def pixela_pixel_update(username, token, graph_id, data_quantity, data_date=datetime.date.today().strftime('%Y%m%d')):
    """Update data to a specified graph today
        username: the name of the user
        token: the token to identify the user

        data_quantity: the quantity to add
        data_date: the date to insert data default is now
    """
    endpoint = f"{HT_PIXELA_ENDPOINT}v1/users/{username}/graphs/{graph_id}/{data_date}"
    header = {
        "X-USER-TOKEN": token
    }
    data = {
        "quantity": data_quantity,
    }
    response = requests.put(url=endpoint, headers=header, json=data)
    print(response.text)


def pixela_pixel_delete(username, token, graph_id, data_date=datetime.date.today().strftime('%Y%m%d')):
    """Delete a specified pixel on specified date
        username: the name of the user
        token: the token to identify the user
        graph_id: the graph identifier
        data_date: the date to insert data default is now
    """
    endpoint = f"{HT_PIXELA_ENDPOINT}v1/users/{username}/graphs/{graph_id}/{data_date}"
    header = {
        "X-USER-TOKEN": token
    }
    response = requests.delete(url=endpoint, headers=header)
    print(response.text)


def main():

    pixela_user_create(username=HT_PIXELA_USERNAME, token=HT_PIXELA_TOKEN)
    pixela_graph_create(username=HT_PIXELA_USERNAME,
                        token=HT_PIXELA_TOKEN,
                        graph_id=HT_GRAPH_ID,
                        graph_name="Cycling Graph",
                        graph_unit="Km",
                        graph_type="float",
                        graph_color="ajisai")
    pixela_pixel_create(username=HT_PIXELA_USERNAME,
                        token=HT_PIXELA_TOKEN,
                        graph_id=HT_GRAPH_ID,
                        data_quantity="35.63")
    pixela_pixel_create(username=HT_PIXELA_USERNAME,
                        token=HT_PIXELA_TOKEN,
                        graph_id=HT_GRAPH_ID,
                        data_quantity="35.63",
                        data_date="20231025")
    pixela_pixel_update(username=HT_PIXELA_USERNAME,
                        token=HT_PIXELA_TOKEN,
                        graph_id=HT_GRAPH_ID,
                        data_quantity="35.63",
                        data_date="20231025")
    pixela_pixel_delete(username=HT_PIXELA_USERNAME,
                        token=HT_PIXELA_TOKEN,
                        graph_id=HT_GRAPH_ID,
                        data_date="20231025")
    pixela_pixel_create_asking(username=HT_PIXELA_USERNAME,
                               token=HT_PIXELA_TOKEN,
                               graph_id=HT_GRAPH_ID)


if __name__ == "__main__":
    main()
