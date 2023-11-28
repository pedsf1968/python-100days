from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

INSTAGRAM_URL = "https://www.instagram.com/"
INSTAGRAM_USERNAME = environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = environ.get("INSTAGRAM_PASSWORD")
INSTAGRAM_ACCOUNT = "keumsong_hanok"
INSTAGRAM_ALL_COOKIES = "Autoriser tous les cookies"
INSTAGRAM_MANDATORY_COOKIES = "Refuser les cookies optionnels"


def select_element_by_text(elements, text):
    for element in elements:
        if element.text == text:
            return element


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        sleep(1)
        # Refuse optionnal cookies
        buttons = self.driver.find_elements(by=By.TAG_NAME, value='button')
        select_element_by_text(buttons, INSTAGRAM_MANDATORY_COOKIES).click()
        sleep(1)

        # Enter username and password
        self.driver.find_element(by=By.NAME, value="username").send_keys(INSTAGRAM_USERNAME, Keys.TAB, INSTAGRAM_PASSWORD, Keys.ENTER)
        sleep(3)

        # Not record credentials
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div').click()
        sleep(5)

        # No notifications
        self.driver.find_element(by=By.CSS_SELECTOR, value='button._a9--._ap36._a9_1').click()
        sleep(5)

    def find_followers(self):
        self.driver.get(f"{INSTAGRAM_URL}/{INSTAGRAM_ACCOUNT}/followers")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click
        sleep(5)

    def follow(self):
        self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div').click()
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


def main():
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()


if __name__ == "__main__":
    main()


