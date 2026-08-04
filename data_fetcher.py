import yfinance as yf


def fetch_company_data(symbol):

    ticker = yf.Ticker(symbol)

    info = ticker.info

    # Historical price data
    history = ticker.history(period="1y")

    historical_prices = []

    for date, row in history.iterrows():
        historical_prices.append(
            {
                "date": str(date.date()),
                "close_price": row["Close"],
                "volume": row["Volume"]
            }
        )

    data = {
        "symbol": symbol,

        # Basic company information
        "company_name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "country": info.get("country"),

        # Market information
        "current_price": info.get("currentPrice"),
        "previous_close": info.get("previousClose"),
        "market_cap": info.get("marketCap"),
        "52_week_high": info.get("fiftyTwoWeekHigh"),
        "52_week_low": info.get("fiftyTwoWeekLow"),

        # Historical data
        "historical_prices": historical_prices
    }

    return data



def fetch_multiple_companies(symbols):

    results = []

    for symbol in symbols:
        data = fetch_company_data(symbol)

        print("=" * 40)
        print("Company:", data["company_name"])
        print("Symbol:", data["symbol"])
        print("Current Price:", data["current_price"])
        print("Market Cap:", data["market_cap"])
        print("52 Week High:", data["52_week_high"])
        print("52 Week Low:", data["52_week_low"])
        print("Historical Records:", len(data["historical_prices"]))

        results.append(data)

    return results



if __name__ == "__main__":

    symbols = [
        "AAPL",
        "MSFT",
        "NVDA"
    ]

    data = fetch_multiple_companies(symbols)

    print("Data fetching completed successfully.")