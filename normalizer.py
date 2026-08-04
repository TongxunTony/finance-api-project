from datetime import datetime


def standardize_record(
    data_source,
    metric_name,
    metric_value,
    units,
    frequency,
    symbol=None,
    observation_date=None,
    retrieval_timestamp=None
):
    """
    Convert raw API data into a common standardized schema.
    """

    return {
        "data_source": data_source,

        "retrieval_timestamp": (
            retrieval_timestamp
            or datetime.now().isoformat()
        ),

        "observation_date": observation_date,

        "symbol": symbol,

        "metric": metric_name,

        "value": metric_value,

        "units": units,

        "frequency": frequency
    }