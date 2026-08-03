import yfinance as yf
from datetime import datetime
import json
import csv
import os

from dotenv import load_dotenv
from fredapi import Fred

from normalizer import standardize_record


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


    records = []


    records.append(
        standardize_record(
            data_source="Yahoo Finance",
            metric_name="current_price",
            metric_value=info.get("currentPrice"),
            units="USD",
            frequency="daily",
            symbol="AAPL"
        )
    )


    records.append(
        standardize_record(
            data_source="Yahoo Finance",
            metric_name="previous_close",
            metric_value=info.get("previousClose"),
            units="USD",
            frequency="daily",
            symbol="AAPL"
        )
    )


    records.append(
        standardize_record(
            data_source="Yahoo Finance",
            metric_name="market_cap",
            metric_value=info.get("marketCap"),
            units="USD",
            frequency="daily",
            symbol="AAPL"
        )
    )


    records.append(
        standardize_record(
            data_source="Yahoo Finance",
            metric_name="52_week_high",
            metric_value=info.get("fiftyTwoWeekHigh"),
            units="USD",
            frequency="daily",
            symbol="AAPL"
        )
    )


    records.append(
        standardize_record(
            data_source="Yahoo Finance",
            metric_name="52_week_low",
            metric_value=info.get("fiftyTwoWeekLow"),
            units="USD",
            frequency="daily",
            symbol="AAPL"
        )
    )


    records.append(
        standardize_record(
            data_source="FRED",
            metric_name="GDP",
            metric_value=fred_data["GDP"],
            units="USD",
            frequency="quarterly",
            symbol=None
        )
    )


    records.append(
        standardize_record(
            data_source="FRED",
            metric_name="CPI",
            metric_value=fred_data["CPI"],
            units="index",
            frequency="monthly",
            symbol=None
        )
    )


    return records



def export_files(data):

    with open("financial_snapshot.json", "w") as f:
        json.dump(data, f, indent=4)


    with open("financial_snapshot.csv", "w", newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=data[0].keys()
        )

        writer.writeheader()

        writer.writerows(data)



if __name__ == "__main__":

    snapshot = generate_snapshot()

    print(json.dumps(snapshot, indent=4))

    export_files(snapshot)

    print("Files exported successfully!")