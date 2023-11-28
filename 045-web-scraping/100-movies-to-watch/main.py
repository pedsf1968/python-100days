import requests
from bs4 import BeautifulSoup

BEST_MOVIES_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
BEST_MOVIES_FILE = "movies.txt"
# Write your code below this line 👇


def main():
    response = requests.get(BEST_MOVIES_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    anchor_list = soup.select(selector=".entity-info-items__list a")

    with open(file=BEST_MOVIES_FILE, mode='w') as file:
        counter = 1
        for anchor in anchor_list:
            movie = anchor.get("data-test")
            file.write(f"{counter}) {movie}\n")
            counter += 1


if __name__ == "__main__":
    main()

