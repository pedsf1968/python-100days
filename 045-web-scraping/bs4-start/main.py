from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()
    soup = BeautifulSoup(contents, 'html.parser')


def get_all_content():
    # display all file content
    print(soup)

    # same but prettier
    print(soup.prettify())


def get_first_tags():
    # Get title tag
    print("All <title> tag: ", soup.title)

    # Get only <title> tag content
    print("<title> content: ", soup.title.string)
    print("First <a> tag: ", soup.a)
    print("First <li> tag: ", soup.li)
    print("First <p> tag: ", soup.p)


def get_all_tags():
    all_anchors_tags = soup.find_all(name="a")
    for tag in all_anchors_tags:
        # print(tag.getText())
        print(tag.get("href"))


def get_all_by_attribute():
    # Get the first tag <h1> with attribute id=name
    heading = soup.find(name="h1", id="name")
    print(heading)

    section_heading = soup.find(name="h3", class_="heading")
    print(section_heading)
    print(section_heading.getText())
    print(section_heading.name)


def get_specific_tag():
    # User CSS selectors
    # select first anchor in paragraph
    company_url = soup.select_one(selector="p a").get("href")
    print(company_url)

    # select first id = name
    name = soup.select_one(selector="#name").string
    print(name)

    # Get the list of heading class
    headings = soup.select(selector=".heading")
    print(headings)


def main():
    # get_all_content()
    # get_first_tags()
    # get_all_tags()
    get_all_by_attribute()
    get_specific_tag()


if __name__ == "__main__":
    main()