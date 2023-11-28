# https://myhttpheader.com/ to get header
import lxml
import requests
import smtplib
from bs4 import BeautifulSoup
from os import environ

AMAZON_URL = "https://www.amazon.fr/CR-1020F-programmes-casserole-int%C3%A9rieure-antiadh%C3%A9sive/dp/B0BDSMYWB1?ref_=ast_sto_dp"
AMAZON_PAGE_FILE = "amazon.html"
HEADER_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
HEADER_ACCEPT_LANGUAGE = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
HEADER_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
HEADER_ACCEPT_ENCODING = "gzip,deflate,br"
TARGET_PRICE = 139


class AmazonProduct:
    def __init__(self, url, target, price=0):
        self.url = url
        self.title = ""
        self.monetary_symbol = "€"
        self.price = price
        self.target = target
        self.web_page = ""

    def get_amazon_page(self):
        headers = {
            "User-Agent": HEADER_USER_AGENT,
            "Accept-Language": HEADER_ACCEPT_LANGUAGE,
            "Accept": HEADER_ACCEPT,
            "Accept-Encoding": HEADER_ACCEPT_ENCODING
        }
        self.web_page = requests.get(url=self.url, headers=headers)

    def save_to_file(self, file_name=AMAZON_PAGE_FILE):
        with open(file_name, "w") as file:
            file.write(self.web_page)

    def read_from_file(self, file_name=AMAZON_PAGE_FILE):
        with open(file_name, "r") as file:
            self.web_page = file.read()

    def get_datas(self):
        soup = BeautifulSoup(self.web_page, 'lxml')
        self.title = soup.find(id="productTitle").get_text().strip()
        self.monetary_symbol = soup.find(class_="a-price-symbol").getText()
        price = soup.find(class_="a-offscreen").getText().split(self.monetary_symbol)[0]
        # The price string use "," and not a "."
        self.price = float(price.replace(",", "."))

    def is_lower(self):
        return self.price < self.target


def send_notification(title, message):
    smtp_password = environ["SMTPLIB_PASSWORD"]
    with smtplib.SMTP(environ["SMTPLIB_SMTP_SERVER"]) as connection:
        connection.starttls()
        connection.login(user=environ["SMTPLIB_EMAIL"], password=smtp_password)
        connection.sendmail(from_addr=environ["SMTPLIB_EMAIL"],
                            to_addrs=environ["SMTPLIB_EMAIL"],
                            msg=f"Subject:{title}\n\n{message}".encode('utf-8')
                            )


def main():
    amazon_product = AmazonProduct(AMAZON_URL, target=TARGET_PRICE)
    # Commented because of Captchat
    # amazon_product.get_amazon_page()
    # amazon_product.save_to_file()
    amazon_product.read_from_file()
    amazon_product.get_datas()
    if amazon_product.is_lower():
        send_notification(title="Amazon Price Alert!",
                          message=f"{amazon_product.title} is now {amazon_product.price}\n{amazon_product.url}")


if __name__ == "__main__":
    main()
