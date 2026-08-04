import yfinance as yf
from datetime import datetime
import json
import csv
import os

from dotenv import load_dotenv

from normalizer import standardize_record
from economic_fetcher import fetch_economic_indicators


load_dotenv()

def generate_snapshot():

    ticker = yf.Ticker("AAPL")

    info = ticker.info

    economic_data = fetch_economic_indicators()

    print(type(economic_data))
    print(economic_data)

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

    for item in economic_data:
        records.append(
        standardize_record(
            data_source=item["data_source"],
            metric_name=item["metric"],
            metric_value=item["value"],
            units=item["units"],
            frequency=item["frequency"],
            symbol=item["series_id"]
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