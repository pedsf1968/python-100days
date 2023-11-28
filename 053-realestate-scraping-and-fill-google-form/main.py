from real_estate import RealEstate
from google_form import GoogleForm


def main():
    # Scraping Real Estate site
    scraper_bot = RealEstate()
    scraper_bot.scraping()
    scraper_bot.display()

    # Fill Google Form with datas
    form_bot = GoogleForm(data=scraper_bot.advertisements)
    form_bot.fill()
    form_bot.driver.quit()


if __name__ == "__main__":
    main()
