import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import json
from datetime import datetime


st.set_page_config(
    page_title="Financial Comparison Dashboard",
    layout="wide"
)


st.title("📊 Multi-Company Financial Comparison Dashboard")


companies = st.multiselect(
    "Select Companies",
    ["AAPL", "MSFT", "NVDA"],
    default=["AAPL", "MSFT", "NVDA"]
)


if len(companies) == 0:
    st.warning("Please select at least one company.")
    st.stop()


data = []

for symbol in companies:

    ticker = yf.Ticker(symbol)
    info = ticker.fast_info


    data.append({

        "Symbol": symbol,

        "Company": info.get(
            "longName",
            symbol
        ),

        "Price": info.get(
            "currentPrice"
        ),

        "Market Cap": info.get(
            "marketCap"
        ),

        "52 Week High": info.get(
            "fiftyTwoWeekHigh"
        ),

        "52 Week Low": info.get(
            "fiftyTwoWeekLow"
        )

    })


df = pd.DataFrame(data)



st.subheader("Key Metrics")


selected_company = companies[0]

selected_info = yf.Ticker(
    selected_company
).info



col1, col2, col3, col4 = st.columns(4)



with col1:

    st.metric(
        "Current Price",
        f"${selected_info.get('currentPrice')}"
    )


with col2:

    market_cap = selected_info.get(
        "marketCap"
    )

    if market_cap:
        market_cap = f"{market_cap/1e12:.2f}T"

    st.metric(
        "Market Cap",
        market_cap
    )


with col3:

    st.metric(
        "52 Week High",
        f"${selected_info.get('fiftyTwoWeekHigh')}"
    )


with col4:

    st.metric(
        "52 Week Low",
        f"${selected_info.get('fiftyTwoWeekLow')}"
    )



st.subheader("Company Comparison")

st.table(df)


st.subheader("Historical Price")


selected_stock = st.selectbox(
    "Choose Stock",
    companies
)



history = yf.Ticker(
    selected_stock
).history(
    period="1y"
)



fig = px.line(

    history,

    x=history.index,

    y="Close",

    title=f"{selected_stock} Price"

)



st.plotly_chart(
    fig,
    use_container_width=True
)



st.subheader("Financial Analysis")

period_choice = st.selectbox(
    "Select Time Range",
    ["1mo", "3mo", "6mo", "1y", "5y"]
)

analysis = yf.Ticker(
    selected_stock
).history(
    period=period_choice
)


analysis["Daily Return"] = (
    analysis["Close"]
    .pct_change()
)



total_return = (

    analysis["Close"].iloc[-1]

    /

    analysis["Close"].iloc[0]

    - 1

)


benchmark = yf.Ticker("^GSPC").history(
    period=period_choice
)

benchmark_return = (
    benchmark["Close"].iloc[-1]
    /
    benchmark["Close"].iloc[0]
    - 1
)



outperformance = total_return - benchmark_return

avg_daily_return = (

    analysis["Daily Return"]
    .mean()

)



volatility = (

    analysis["Daily Return"]
    .std()

)



high_52 = selected_info.get(
    "fiftyTwoWeekHigh"
)


current_price = selected_info.get(
    "currentPrice"
)


distance_high = (

    current_price / high_52 - 1

)



c1, c2, c3, c4, c5, c6 = st.columns(6)



with c1:

    st.metric(
        "Total Return",
        f"{total_return:.2%}"
    )


with c2:

    st.metric(
        "Average Daily Return",
        f"{avg_daily_return:.4%}"
    )


with c3:

    st.metric(
        "Volatility",
        f"{volatility:.2%}"
    )


with c4:

    st.metric(
        "Distance from 52W High",
        f"{distance_high:.2%}"
    )

with c5:
    st.metric(
        "S&P500 Return",
        f"{benchmark_return:.2%}"
    )


with c6:
    st.metric(
        "Outperformance",
        f"{outperformance:.2%}"
    )


st.subheader("Download Data")


export_data = df.copy()


csv = export_data.to_csv(
    index=False
)


json_data = export_data.to_json(
    orient="records",
    indent=4
)



st.download_button(

    label="Download CSV",

    data=csv,

    file_name="company_comparison.csv",

    mime="text/csv"

)



st.download_button(

    label="Download JSON",

    data=json_data,

    file_name="company_comparison.json",

    mime="application/json"

)


st.subheader("Economic Indicators")

economic_df = pd.DataFrame(
    {
        "Indicator": [
            "GDP",
            "CPI",
            "Unemployment Rate",
            "Federal Funds Rate"
        ],
        "Value": [
            32475.21,
            332.568,
            4.2,
            3.63
        ],
        "Frequency": [
            "Quarterly",
            "Monthly",
            "Monthly",
            "Monthly"
        ]
    }
)

st.dataframe(economic_df)

st.bar_chart(
    economic_df.set_index("Indicator")["Value"]
)

st.success(
    "Dashboard loaded successfully!"
)