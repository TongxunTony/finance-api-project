import yfinance as yf
import numpy as np


def fetch_company_data(symbol):

    ticker = yf.Ticker(symbol)

    # ---------- basic info ----------
    try:
        info = ticker.info
    except:
        info = {}

    try:
        fast = ticker.fast_info
    except:
        fast = {}


    # company name fallback
    company_name = (
        info.get("longName")
        or info.get("shortName")
        or symbol
    )


    # price fallback
    current_price = (
        fast.get("last_price")
        or fast.get("lastPrice")
        or info.get("regularMarketPrice")
        or info.get("previousClose")
    )


    # ---------- historical data ----------

    try:
        history = ticker.history(
            period="1y"
        )

    except:
        history = None


    historical_prices = []


    if history is not None and not history.empty:

        for date, row in history.iterrows():

            historical_prices.append(
                {
                    "date": str(date.date()),
                    "close_price": float(row["Close"]),
                    "volume": int(row["Volume"])
                }
            )


    # ---------- volatility ----------

    volatility = None

    if len(historical_prices) > 20:

        prices = [
            x["close_price"]
            for x in historical_prices
        ]

        returns = np.diff(prices) / prices[:-1]

        volatility = float(
            np.std(returns) * np.sqrt(252)
        )


    return {

        "symbol": symbol,

        "company_name": company_name,

        "current_price": current_price,

        "market_cap": info.get(
            "marketCap"
        ),

        "pe_ratio": info.get(
            "trailingPE"
        ),

        "revenue_growth": info.get(
            "revenueGrowth"
        ),

        "profit_margin": info.get(
            "profitMargins"
        ),

        "volatility": volatility,

        "historical_prices":
            historical_prices

    }