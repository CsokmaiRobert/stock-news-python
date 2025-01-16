import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCKS_API_KEY = os.environ.get("STOCKS_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCKS_API_KEY,
    "outputsize": "compact"
}
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()

response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response.raise_for_status()
news_data = response.json()


yesterday_closing_price = stock_data["Time Series (Daily)"]["2024-08-30"]["4. close"]
day_before_yesterday_closing_price = stock_data["Time Series (Daily)"]["2024-08-29"]["4. close"]

difference = round(float(yesterday_closing_price) - float(day_before_yesterday_closing_price), 10)
percentage = round((difference / float(yesterday_closing_price)) * 100, 2)
arrow = "🔺"
if percentage < 0:
    arrow = "🔻"

news = []
if percentage >= 5 or percentage <= -5:
    news = news_data["articles"][:3]
    for i in range(3):
        title = news[i]["title"]
        description = news[i]["description"]
        print(f"{STOCK_NAME}: {arrow}{percentage}%\nHeadline: {title}\nBrief: {description}")

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

