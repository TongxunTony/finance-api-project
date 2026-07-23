import yfinance as yf
from datetime import datetime
import json
import csv
import os

from dotenv import load_dotenv
from fredapi import Fred

load_dotenv()

fred = Fred(
    api_key=os.getenv("FRED_API_KEY")
)

def get_fred_data():

    gdp = fred.get_series_latest_release("GDP").dropna().iloc[-1]

    cpi = fred.get_series_latest_release("CPIAUCSL").dropna().iloc[-1]

    return {
        "GDP": float(gdp),
        "CPI": float(cpi)
    }

def generate_snapshot():

    ticker = yf.Ticker("AAPL")

    info = ticker.info

    fred_data = get_fred_data()

    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "company": "Apple Inc.",
        "symbol": "AAPL",
        "current_price": info.get("currentPrice"),
        "previous_close": info.get("previousClose"),
        "market_cap": info.get("marketCap"),
        "52_week_high": info.get("fiftyTwoWeekHigh"),
        "52_week_low": info.get("fiftyTwoWeekLow"),
        
        "GDP": fred_data["GDP"],
        "CPI": fred_data["CPI"]
    }

    return snapshot


def export_files(data):

    # JSON output
    with open("financial_snapshot.json", "w") as f:
        json.dump(data, f, indent=4)


    # CSV output
    with open("financial_snapshot.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=data.keys()
        )

        writer.writeheader()
        writer.writerow(data)


if __name__ == "__main__":

    snapshot = generate_snapshot()

    print(json.dumps(snapshot, indent=4))

    export_files(snapshot)

    print("Files exported successfully!")