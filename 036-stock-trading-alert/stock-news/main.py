import requests
import os
from datetime import date, timedelta
from twilio.rest import Client


SN_ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
SN_ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
SN_NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"
SN_NEWSAPI_API_KEY = os.environ.get("NEWSAPI_API_KEY")
SN_STOCK = "TSLA"
SN_COMPANY_NAME = "Tesla Inc"
SN_STOCK_VARIATION_THRESHOLD = 2
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_PHONE = os.environ.get("MY_PHONE")

def get_yesterday_stock_variation(company, day):
    day_before = day - timedelta(days=1)
    query_parameters = {
        "function": "TIME_SERIES_DAILY",
        "apikey": SN_ALPHAVANTAGE_API_KEY,
        "symbol": company,
    }

    response = requests.get(url=SN_ALPHAVANTAGE_ENDPOINT, params=query_parameters)
    daily_stock = response.json()['Time Series (Daily)']

    yesterday_close = float(daily_stock[str(day)]["4. close"])
    before_yesterday_close = float(daily_stock[str(day_before)]["4. close"])

    print(before_yesterday_close, yesterday_close)
    return (before_yesterday_close - yesterday_close)*100/before_yesterday_close


def get_yesterday_news(query, day,articles):

    query_parameters = {
        "q":  query,
        "from": day,
        "sortBy": "publishedAt",
        "apiKey": SN_NEWSAPI_API_KEY
    }
    response = requests.get(url=SN_NEWSAPI_ENDPOINT, params=query_parameters)
    return response.json()['articles'][:articles]



def send_message(phone_to: str, message: str, phone_from=TWILIO_PHONE_NUMBER):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    print(auth_token, account_sid)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=phone_from,
        to=phone_to
    )
    print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def main():
    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    # the last information is from 3 days
    last_day = date.today() - timedelta(days=3)
    variation = get_yesterday_stock_variation(company=SN_STOCK, day=last_day)

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    if abs(variation) > SN_STOCK_VARIATION_THRESHOLD:
        news_data = get_yesterday_news(query=SN_COMPANY_NAME, day=last_day, articles=3)
        for news in news_data:
            send_message(phone_to=MY_PHONE, message=f"Variation: {variation}\nTitle: {news['title']}\n{news['description']}")


    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.


if __name__ == "__main__":
    main()