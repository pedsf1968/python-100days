# https://openai.com/blog/openai-api/
# https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?usp=sharing
# https://www.nutritionix.com/business/api
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.gz6pu9o7f9iz
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.zhjgcprrgvim
# https://gist.github.com/angelabauer/dd71d7072626afd728e1730584c6e4b8
# https://sheety.co/

from os import environ
import requests

NUTRITIONIX_NATURAL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_API_ID = environ.get("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = environ.get("NUTRITIONIX_API_KEY")

WT_GENDER = "male"
WT_HEIGHT = "178"
WT_WEIGHT = "90"
WT_AGE = 55


def nutritionix_calculate_calories_from_query(api_id, api_key, query, gender, height, weight, age):
    header = {
        "x-app-id": api_id,
        "x-app-key": api_key,
        "Content-Type": "application/json"
    }
    body = {
        "query": query,
        "gender": gender,
        "weight_kg": weight,
        "height_cm": height,
        "age": age,
    }
    response = requests.post(url=NUTRITIONIX_NATURAL_ENDPOINT, headers=header, json=body)
    return response.json()["exercises"]


def main():
    query = input("Tell me wich exercice you did: ")
    data = nutritionix_calculate_calories_from_query(api_id=NUTRITIONIX_API_ID,
                                                     api_key=NUTRITIONIX_API_KEY,
                                                     query=query,
                                                     gender=WT_GENDER,
                                                     height=WT_HEIGHT,
                                                     weight=WT_WEIGHT,
                                                     age=WT_AGE)


if __name__ == "__main__":
    main()
