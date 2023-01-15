import requests
import math

ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = "JGOCXWF0WBIMKKL7"

NEWS_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": API_KEY
}

response = requests.get(url=ENDPOINT, params=NEWS_PARAMS)
response.raise_for_status()

data = response.json()
print(data)

# yesterday_close = data["Time Series (Daily)"]["2023-01-12"]["4. close"]
# day_before_yesterday_close = data["Time Series (Daily)"]["2023-01-11"]["4. close"]
#
# # print(yesterday_close)
# # print(day_before_yesterday_close)
#
# different = float(yesterday_close) - float(day_before_yesterday_close)

