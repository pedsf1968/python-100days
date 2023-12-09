import requests
from os import environ
from pprint import pprint

DEBUG = False
TMDB_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_MOVIE_DETAIL_URL = "https://api.themoviedb.org/3/movie"
TMDB_API_KEY = environ.get("TMDB_API_KEY")
TMDB_API_TOKEN = environ.get("TMDB_API_KEY")


def tmdb_get_movies(title: str):
    url = TMDB_URL
    params = {"query": f"{title}",
              "include_adult": False,
              "language": "en-US",
              "page": 1
              }
    headers = {"accept": "application/json",
               "Authorization": f"Bearer {TMDB_API_TOKEN}"
               }

    response = requests.get(url=url, headers=headers, params=params).json()
    if DEBUG:
        pprint(params)
        pprint(headers)
        pprint(response)
    return response['results']


def tmdb_get_movie_details(movie_id):
    url = f"{TMDB_MOVIE_DETAIL_URL}/{movie_id}"
    headers = {"accept": "application/json",
               "Authorization": f"Bearer {TMDB_API_TOKEN}"
               }
    params = {"language": "en-US"}

    response = requests.get(url=url, headers=headers, params=params).json()
    if DEBUG:
        print(f"url: {url}")
        pprint(headers)
        pprint(params)
        pprint(response)
    return response


