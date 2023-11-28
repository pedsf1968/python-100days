from selenium import webdriver
from selenium.webdriver.common.by import By

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"


def wikipedia_article_count(driver):
    """ Get Wikipedia article numbers and click on the link
        driver: the browser driver
    """
    driver.get(WIKIPEDIA_URL)
    article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
    # print number of articles
    print(article_count.text)
    # click on the anchor
    article_count.click()


def wikipedia_find_portals(driver):
    """ Click on Community portal of Wikipedia
        driver: the browser driver
    """
    driver.get(WIKIPEDIA_URL)
    all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
    all_portals.click()


def wikipedia_search(driver, key):
    """ Search word on wikipedia
        driver: the browser driver
        key: the word to find abour
    """
    driver.get(WIKIPEDIA_URL)
    search_bar = driver.find_element(By.NAME, "search")
    search_bar.send_keys("Toto")


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    wikipedia_article_count(driver)
    wikipedia_find_portals(driver)
    wikipedia_search(driver, "Python")


if __name__ == "__main__":
    main()
