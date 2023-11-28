from selenium import webdriver
from selenium.webdriver.common.by import By

AMAZON_URL = "https://www.amazon.fr/CR-1020F-programmes-casserole-int%C3%A9rieure-antiadh%C3%A9sive/dp/B0BDSMYWB1?ref_=ast_sto_dp"
AMAZON_PRICE_WHOLE_CLASS = 'a-price-whole'
AMAZON_PRICE_FRACTION_CLASS = 'a-price-fraction'
PYTHON_URL = "https://www.python.org/"
PYTHON_SEARCH_NAME = "q"
PYTHON_SUBMIT_ID = "submit"
PYTHON_LINK_SELECTOR = ".documentation-widget a"
PYTHON_LINK_XPATH = '//*[@id="site-map"]/div[2]/div/ul/li[3]/a'


def main():
    # To keep browser open after program finish
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    # driver.get(AMAZON_PRICE_WHOLE_CLASS)
    # price_whole = driver.find_element(By.CLASS_NAME, AMAZON_PRICE_WHOLE_CLASS).text
    # price_fraction = driver.find_element(By.CLASS_NAME, AMAZON_PRICE_FRACTION_CLASS).text
    # print(f"The price is {price_whole},{price_fraction}")

    driver.get(PYTHON_URL)
    element = driver.find_element(By.NAME, value=PYTHON_SEARCH_NAME)
    print(f"Tag name: {element.tag_name}")
    print(f"Attribute: {element.get_attribute('placeholder')}")

    button = driver.find_element(By.ID, value=PYTHON_SUBMIT_ID)
    print(f"Button size: {button.size}")

    documentation_link = driver.find_element(By.CSS_SELECTOR, value=PYTHON_LINK_SELECTOR)
    print(f"Link: {documentation_link.text}")

    bug_link = driver.find_element(By.XPATH, value=PYTHON_LINK_XPATH)
    print(f"Bug link: {bug_link.text}")

    # Get all Upcoming Events
    upcoming_dict = {}
    # upcoming_elements = driver.find_elements(By.TAG_NAME, value="time")

    xpath = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li'
    time_elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
    name_elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

    for index in range(len(time_elements)):
        upcoming_dict[index] = {
            "time": time_elements[index].text,
            "name": name_elements[index].text,
        }

    print(upcoming_dict)
    # Close a tab
    # driver.close()
    # close browser
    driver.quit()


if __name__ == "__main__":
    main()
