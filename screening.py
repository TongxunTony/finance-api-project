from data_fetcher import fetch_company_data
from risk_scoring import calculate_risk_score



def screen_companies(symbols):

    results = []


    for symbol in symbols:

        try:

            data = fetch_company_data(
                symbol
            )

            score = calculate_risk_score(
                data
            )


            results.append(score)


        except Exception as e:

            results.append(
                {
                    "symbol": symbol,
                    "error": str(e)
                }
            )


    return results