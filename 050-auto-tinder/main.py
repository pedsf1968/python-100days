from selenium import webdriver
from selenium.webdriver.common.by import By
from os import environ
import time
import datetime

TINDER_URL = "https://tinder.com/app/recs"
TINDER_EMAIL = environ.get("TINDER_EMAIL")
TINDER_PASS = environ.get("TINDER_PASS")
TINDER_DECISION = "NO"
TINDER_SWIPE_COUNT = 5


def tinder_connection(driver):
    # Accept Tinder Cookies
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button').click()

    # Connection button
    driver.find_element(by=By.LINK_TEXT, value='Connexion').click()
    time.sleep(3)

    # Facebook button
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()
    time.sleep(5)

    # Switch to facebook window
    windows = driver.window_handles
    driver.switch_to.window(window_name=windows[1])

    # Refuse Facebook Cookies
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[1]').click()

    # Enter credentials
    driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(TINDER_EMAIL)
    driver.find_element(by=By.XPATH, value='//*[@id="pass"]').send_keys(TINDER_PASS)
    driver.find_element(by=By.NAME, value="login").click()

    # Switch to initial window
    driver.switch_to.window(window_name=windows[0])
    time.sleep(5)

    # Allow location access
    driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
    time.sleep(4)

    # Refuse notifications
    driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]').click()


def tinder_swipe(driver, decision=TINDER_DECISION, swipe_count=TINDER_SWIPE_COUNT):
    if decision == "yes":
        # Swipe no
        value = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button'
    else:
        # Swipe no
        value = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button'
    for _ in range(swipe_count):
        driver.find_element(by=By.XPATH, value=value)


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(TINDER_URL)

    tinder_connection(driver=driver)
    tinder_swipe(driver=driver, decision="NO", swipe_count=1)
    driver.quit()


if __name__ == "__main__":
    main()
