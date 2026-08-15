def calculate_risk_score(data):

    score = 100


    volatility = data.get(
        "volatility"
    )

    pe = data.get(
        "pe_ratio"
    )


    # volatility risk

    if volatility is not None:

        if volatility > 0.35:
            score -= 25

        elif volatility > 0.20:
            score -= 10


    # valuation risk

    if pe is not None:

        if pe > 50:
            score -= 15

        elif pe > 30:
            score -= 5


    if score >= 80:

        level = "Low"

    elif score >= 60:

        level = "Medium"

    else:

        level = "High"



    return {

        "symbol":
            data["symbol"],

        "company_name":
            data["company_name"],

        "price":
            data["current_price"],

        "risk_score":
            score,

        "risk_level":
            level

    }