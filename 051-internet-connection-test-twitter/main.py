from selenium import webdriver
from selenium.webdriver.common.by import By
from os import environ
import time

# Service provider speed to check in Mbps
PROMISE_DOWN = 11
PROMISE_UP = 1
SPEEDTEST_URL = "https://www.speedtest.net/"
X_URL = "https://twitter.com/login"
X_EMAIL = environ.get("X_EMAIL")
X_PASSWORD = environ.get("X_PASSWORD")
X_NICKNAME = environ.get("X_NICKNAME")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.provider = ""
        self.network = "ADSL"
        self.up = 0
        self.down = 0
        self.ping_speed = 0
        self.download_latency = 0
        self.upload_latency = 0

    def display(self):
        print(f"Internet test speed result:\n"
              f"Provider: {self.provider} on {self.network} connection.\n"
              f"Ping speed: {self.ping_speed}\n"
              f"Down: {self.down} latency: {self.download_latency}\n"
              f"Up: {self.up} latency: {self.upload_latency}")

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        # Accept collecting datas
        self.driver.find_element(by=By.CSS_SELECTOR, value="#onetrust-consent-sdk #onetrust-accept-btn-handler").click()

        # Launch test
        self.driver.find_element(by=By.CLASS_NAME, value="start-text").click()
        time.sleep(60)
        # Close popup window
        self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button').click()
        self.down = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        self.provider = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]').text
        self.ping_speed = self.driver.find_element(by=By.CLASS_NAME, value='ping-speed').text
        self.download_latency = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[3]/span').text
        self.upload_latency = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[4]/span').text

    def tweet_at_provider(self):
        self.driver.get(X_URL)
        time.sleep(2)

        # Enter email
        self.driver.find_element(by=By.NAME, value='text').send_keys(X_EMAIL)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        time.sleep(1)

        # Enter user nickname
        self.driver.find_element(by=By.NAME, value='text').send_keys(X_NICKNAME)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        time.sleep(1)

        # Enter password
        self.driver.find_element(by=By.NAME, value='password').send_keys(X_PASSWORD)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        time.sleep(1)

        # Enter post
        post = self.driver.find_element(by=By.XPATH,
                                        value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        message = (f"www.speedtest.net Bot\n"
                   f"Provider: {self.provider} on {self.network} connection.\n"
                   f"Ping speed: {self.ping_speed}\n"
                   f"Down: {self.down} latency: {self.download_latency}\n"
                   f"Up: {self.up} latency: {self.upload_latency}")
        post.send_keys(message)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]').click()


def main():
    internet_speed_bot = InternetSpeedTwitterBot()
    internet_speed_bot.get_internet_speed()
    internet_speed_bot.display()
    internet_speed_bot.tweet_at_provider()
    internet_speed_bot.driver.quit()


if __name__ == "__main__":
    main()