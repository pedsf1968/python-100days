from selenium import webdriver
from selenium.webdriver.common.by import By
REAL_ESTATE_URL = "https://appbrewery.github.io/Zillow-Clone/"


class RealEstate:
    """Class to scrap a real estate Zillow-Clone site and get announces"""
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(REAL_ESTATE_URL)
        self.advertisements = []

    def display(self):
        """Display class content"""
        for item in self.advertisements:
            print(f"Price: {item['price']}\n"
                  f"Link: {item['link']}\n"
                  f"Address: {item['address']}\n"
                  f"Description: {item['description']}")

    def scraping(self):
        """Scraping web site"""
        articles = self.driver.find_elements(by=By.TAG_NAME, value='article')
        for article in articles:
            advertisement = {
                "price": article.find_element(by=By.CSS_SELECTOR, value='div .PropertyCardWrapper').text[:6],
                "link": article.find_element(by=By.TAG_NAME, value='a').get_attribute("href"),
                "address": article.find_element(by=By.TAG_NAME, value='a').text,
                "description": article.find_element(by=By.TAG_NAME, value='ul').text
            }
            self.advertisements.append(advertisement)
        # Close browser
        self.driver.quit()
