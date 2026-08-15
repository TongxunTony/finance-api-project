def calculate_risk_score(data):

    score = 100
    risk_flags = []


    # Get financial metrics safely
    volatility = data.get("volatility")
    pe = data.get("pe_ratio")
    profit_margin = data.get("profit_margin")
    revenue_growth = data.get("revenue_growth")
    market_cap = data.get("market_cap")


    # Missing data check
    required_fields = [
        "current_price",
        "market_cap",
        "pe_ratio",
        "revenue_growth",
        "profit_margin",
        "volatility"
    ]

    missing_fields = []

    for field in required_fields:
        if data.get(field) is None:
            missing_fields.append(field)

    if len(missing_fields) > 0:
        risk_flags.append(
            "Missing data: " + ", ".join(missing_fields)
        )
        score -= 5


    # Volatility risk
    if volatility is not None:

        if volatility > 0.35:
            score -= 25
            risk_flags.append("High stock volatility")

        elif volatility > 0.20:
            score -= 10
            risk_flags.append("Moderate stock volatility")


    # Valuation risk
    if pe is not None:

        if pe > 50:
            score -= 15
            risk_flags.append("High valuation risk")

        elif pe > 30:
            score -= 5
            risk_flags.append("Moderate valuation risk")


    # Profitability risk
    if profit_margin is not None:

        if profit_margin < 0:
            score -= 15
            risk_flags.append("Negative profit margin")

        elif profit_margin < 0.10:
            score -= 5
            risk_flags.append("Low profit margin")


    # Revenue growth risk
    if revenue_growth is not None:

        if revenue_growth < 0:
            score -= 10
            risk_flags.append("Negative revenue growth")


    # Market capitalization check
    if market_cap is not None:

        if market_cap < 10_000_000_000:
            score -= 5
            risk_flags.append("Smaller market capitalization")


    # If no major flags
    if len(risk_flags) == 0:
        risk_flags.append("No major risk flags detected")


    # Keep score within 0 to 100
    score = max(0, min(score, 100))


    # Risk level
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
            level,

        "risk_flags":
            risk_flags
    }