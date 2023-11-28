from selenium import webdriver
from selenium.webdriver.common.by import By
from os import environ
import time

LINKEDIN_URL = "https://linkedin.com/"
LINKEDIN_SEARCH_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3734820994&f_E=2&geoId=&keywords=Devops%20Engineer&location=France&origin=JOB_SEARCH_PAGE_JOB_FILTER"
LINKEDIN_EMAIL = environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = environ.get("LINKEDIN_PASSWORD")


def linkedin_init(driver):
    # Click sign
    identify = driver.find_element(by=By.XPATH, value= '/html/body/div[3]/header/nav/div/a[2]')
    identify.click()
    # enter username and pw
    username = driver.find_element(by=By.ID, value="username")
    username.send_keys(LINKEDIN_EMAIL)
    password = driver.find_element(by=By.ID, value="password")
    password.send_keys(LINKEDIN_PASSWORD)
    # Validate signing
    identify = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
    identify.click()


def linkedin_apply_for_a_job(driver):
    apply_button = driver.find_element(by=By.CLASS_NAME, value='jobs-apply-button')
    apply_button.click()
    apply_button = driver.find_element(by=By.CLASS_NAME, value='jobs-apply-button')
    apply_button.click()


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(LINKEDIN_SEARCH_URL)
    linkedin_init(driver)
    time.sleep(2)
    linkedin_apply_for_a_job(driver)

    # driver.quit()


if __name__ == "__main__":
    main()
