from datetime import datetime


def standardize_record(
    data_source,
    metric_name,
    metric_value,
    units,
    frequency,
    symbol=None,
    timestamp=None
):
    """
    Convert raw API data into a common standardized schema.
    """

    return {
        "data_source": data_source,
        "timestamp": timestamp or datetime.now().isoformat(),
        "symbol": symbol,
        "metric_name": metric_name,
        "metric_value": metric_value,
        "units": units,
        "frequency": frequency
    }
