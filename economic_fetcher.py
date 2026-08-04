import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"


def fetch_fred_series(series_id, name, units, frequency):
    """
    Fetch one economic indicator from FRED
    """

    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 1
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    observation = data["observations"][0]

    return {
        "data_source": "FRED",
        "retrieval_timestamp": datetime.now().isoformat(),
        "observation_date": observation["date"],
        "series_id": series_id,
        "metric": name,
        "value": observation["value"],
        "units": units,
        "frequency": frequency
    }


def fetch_economic_indicators():

    indicators = []

    indicators.append(
        fetch_fred_series(
            "GDP",
            "Gross Domestic Product",
            "Billions of Dollars",
            "Quarterly"
        )
    )

    indicators.append(
        fetch_fred_series(
            "CPIAUCSL",
            "Consumer Price Index",
            "Index",
            "Monthly"
        )
    )

    indicators.append(
        fetch_fred_series(
            "UNRATE",
            "Unemployment Rate",
            "Percent",
            "Monthly"
        )
    )

    indicators.append(
        fetch_fred_series(
            "FEDFUNDS",
            "Federal Funds Rate",
            "Percent",
            "Monthly"
        )
    )

    return indicators


if __name__ == "__main__":

    results = fetch_economic_indicators()

    for item in results:
        print("=" * 40)
        print(item)