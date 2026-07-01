import os
import json
import requests
import yfinance as yf
from dotenv import load_dotenv
from fredapi import Fred

load_dotenv()

fred_api_key = os.getenv("FRED_API_KEY")
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")


def test_fred():
    fred = Fred(api_key=fred_api_key)
    data = fred.get_series_latest_release("GDP")
    latest_value = data.dropna().iloc[-1]

    return {
        "source": "FRED",
        "series": "GDP",
        "latest_value": float(latest_value),
        "status": "success"
    }


def test_yahoo_finance():
    ticker = yf.Ticker("AAPL")
    history = ticker.history(period="5d")
    latest_close = history["Close"].iloc[-1]

    return {
        "source": "Yahoo Finance",
        "symbol": "AAPL",
        "latest_close": float(latest_close),
        "status": "success"
    }


def test_alpha_vantage():
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": "AAPL",
        "apikey": alpha_vantage_api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "source": "Alpha Vantage",
        "symbol": "AAPL",
        "raw_response": data,
        "status": "success"
    }


def main():
    results = {
        "fred": test_fred(),
        "yahoo_finance": test_yahoo_finance(),
        "alpha_vantage": test_alpha_vantage()
    }

    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()