from selenium import webdriver
from selenium.webdriver.common.by import By
import time

DASHNET_COOKIE_CLICKER = "https://orteil.dashnet.org/cookieclicker/"
DASHNET_COOKIE_CLICKER_LANGUAGE = "langSelect-FR"
DASHNET_COOKIE_CLICKER_SHORT_PERIOD = 10
DASHNET_COOKIE_CLICKER_LONG_PERIOD = 1*60

def cookie_init(driver):
    """ Removes pop-up and select language """
    button = driver.find_element(by=By.CLASS_NAME, value="fc-button-label")
    button.click()
    time.sleep(2)
    got_it_button = driver.find_element(by=By.CLASS_NAME, value="cc_btn_accept_all")
    got_it_button.click()
    time.sleep(3)
    french_button = driver.find_element(by=By.ID, value=DASHNET_COOKIE_CLICKER_LANGUAGE)
    french_button.click()
    time.sleep(3)


def cookie_get_store_element(driver):
    item_prices = []

    for price in driver.find_elements(by=By.CSS_SELECTOR, value="#products .unlocked .price"):
        item_prices.append(int(price.text.replace(",", "")))
    return item_prices


def cookie_get_number(driver):
    text = driver.find_element(by=By.ID, value="cookies").text
    text = text.replace(",", "").split(" ")[0]
    return int(text)


def cookie_select_product(driver, prices, money):
    product_id = "product" + str(len(prices) - 1)
    product = driver.find_element(by=By.ID, value=product_id)
    product.click()


def cookie_clicker(driver):
    cookie_button = driver.find_element(by=By.ID, value="bigCookie")

    short_timeout = time.time() + DASHNET_COOKIE_CLICKER_SHORT_PERIOD
    long_timeout = time.time() + DASHNET_COOKIE_CLICKER_LONG_PERIOD

    while True:
        cookie_button.click()

        if time.time() > short_timeout:
            item_prices = cookie_get_store_element(driver)
            cookies = cookie_get_number(driver)
            cookie_select_product(driver, item_prices, cookies)
            short_timeout = time.time() + DASHNET_COOKIE_CLICKER_SHORT_PERIOD

        if time.time() > long_timeout:
            text = driver.find_element(by=By.ID, value="cookies").text
            text = text.split(":")[1]
            print(f"{text} cookies by seconds ")
            break


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(DASHNET_COOKIE_CLICKER)
    cookie_init(driver)
    cookie_clicker(driver)


if __name__ == "__main__":
    main()
