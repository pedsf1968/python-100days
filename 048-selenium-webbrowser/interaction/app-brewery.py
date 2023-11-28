# Application to auto register
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

APP_BREWERY_URL = "https://secure-retreat-92358.herokuapp.com/"


def app_brewery(driver):
    driver.get(APP_BREWERY_URL)
    first_name = driver.find_element(By.NAME, "fName")
    first_name.send_keys("Paul-Emmanuel")
    last_name = driver.find_element(By.NAME, "lName")
    last_name.send_keys("DSF")
    email = driver.find_element(By.NAME, "email")
    email.send_keys("pedsf@gmail.com")
    button = driver.find_element(By.TAG_NAME, "button")
    button.send_keys(Keys.ENTER)


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    app_brewery(driver)


if __name__ == "__main__":
    main()
