import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHAVANTAGE_API_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = "7OYJTT2YG8DOQK7K"

NEWSAPI_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWSAPI_API_KEY = "87168d8fa4784f0ea261465d65877f38"

MY_EMAIL = "secret"
MY_PASSWORD = "secret"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

stock_response = requests.get(ALPHAVANTAGE_API_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = list(stock_data.values())

yesterday_data = stock_data_list[0]
yesterday_stock_close_price = float(yesterday_data["4. close"])

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_stock_close_price = float(day_before_yesterday_data["4. close"])

diff_ratio = abs(yesterday_stock_close_price - day_before_yesterday_stock_close_price) / yesterday_stock_close_price

if diff_ratio >= 0.05:

    stock_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWSAPI_API_KEY,
    }

    news_response = requests.get(NEWSAPI_API_ENDPOINT, params=stock_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    title_description = [[i["title"], i["description"]] for i in three_articles]
    formatted_articles = [f"Subject:Headline: {article['title']}.\n\nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # makes connection secure
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="secret",
                msg=article,
            )
