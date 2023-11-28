from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScCSMRs5hNaJMJOUIbQmK9Qt56n0rDZx7aXrs65sSZnmqTyMQ/viewform?usp=sf_link"


class GoogleForm:
    """Class to fill Google Form with datas"""
    def __init__(self, data):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.data = data

    def display(self):
        """Display class content"""
        for item in self.data:
            print(f"Price: {item['price']}\n"
                  f"Link: {item['link']}\n"
                  f"Address: {item['address']}\n"
                  f"Description: {item['description']}")

    def fill(self):
        """Fill Google Form with datas"""
        self.driver.get(GOOGLE_FORM_URL)
        sleep(3)

        for item in self.data:
            fields = self.driver.find_elements(by=By.CSS_SELECTOR, value='input.whsOnd.zHQkBf')
            fields[0].send_keys(item['address'])
            fields[1].send_keys(item['price'])
            fields[2].send_keys(item['description'])
            fields[3].send_keys(item['link'])
            self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
            sleep(2)
            self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
            sleep(2)
        # close form windows when done
        self.driver.close()

