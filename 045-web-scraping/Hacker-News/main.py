# https://news.ycombinator.com/
from bs4 import BeautifulSoup
import requests

WEBSITE_URL = "https://news.ycombinator.com/news"

articles = []


def find_max(object_list, attribute_name):
    object_max = ""
    attribute_max = 0

    for object in object_list:
        attribute = object[attribute_name]
        if attribute > attribute_max:
            object_max = object
            attribute_max = attribute
    return object_max


def object_list_sorted(object_list, attribute_name):
    sorted_list = []
    while len(object_list) != 0:
        object = find_max(object_list, attribute_name)
        sorted_list.append(object)
        object_list.remove(object)
    return sorted_list


def main():
    response = requests.get(WEBSITE_URL)
    contents = response.text
    soup = BeautifulSoup(contents, "html.parser")
    # get texts and links in <a>
    anchor_list = soup.find_all(name="a", rel="noreferrer")
    # get scores in <span>
    upvote_list = soup.find_all(name="span", class_="score")

    # loop on two lists
    for anchor, upvote in zip(anchor_list, upvote_list):
        # get score in integer
        score = int(upvote.getText().split()[0])
        # create object and save it in list
        article = {
            "text": anchor.getText(),
            "link": anchor.get("href"),
            "votes": score
        }
        articles.append(article)

    sorted_articles = object_list_sorted(articles, "votes")
    for article in sorted_articles:
        print(f"{article['votes']}: {article['text']} {article['link']}")


if __name__ == "__main__":
    main()