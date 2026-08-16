# Investment Risk Scoring Tool

## Overview

This project builds an investment screening and risk scoring tool that evaluates multiple companies using financial data from Yahoo Finance.

The system collects company financial information, analyzes multiple financial factors, calculates an overall risk score, and classifies companies into different risk levels.

The goal of this project is to provide a simple framework for comparing companies based on financial performance and investment risk.

---

## Features

- Fetches financial data from Yahoo Finance
- Supports multiple company analysis
- Calculates investment risk scores
- Evaluates multiple financial indicators
- Classifies companies into Low, Medium, and High risk levels
- Provides comparison results between different companies

---

## Companies Tested

The tool evaluates the following five companies:

| Symbol | Company |
|---|---|
| AAPL | Apple Inc. |
| MSFT | Microsoft Corporation |
| NVDA | NVIDIA Corporation |
| GOOGL | Alphabet Inc. |
| AMZN | Amazon.com Inc. |

---

## Financial Factors

The risk assessment considers multiple financial factors:

### Current Stock Price

The latest available stock price is collected for each company.

### Market Capitalization

Market capitalization is used to represent company size and market value.

### Price-to-Earnings Ratio (P/E Ratio)

The P/E ratio is used to evaluate valuation risk.

A higher P/E ratio may indicate higher valuation risk.

### Revenue Growth

Revenue growth is considered as an indicator of business expansion and company performance.

### Profit Margin

Profit margin is used to evaluate profitability and operational efficiency.

### Stock Volatility

Historical stock prices are analyzed to calculate stock volatility.

Higher volatility indicates higher market risk.

---

## Risk Scoring Method

The risk score starts from 100 points.

The score is adjusted according to different risk factors:

- Higher stock volatility increases risk
- Higher P/E ratio increases valuation risk

The final risk score is classified into three categories:

| Risk Score | Risk Level |
|---|---|
| 80 - 100 | Low Risk |
| 60 - 79 | Medium Risk |
| Below 60 | High Risk |

A higher score represents lower investment risk.
---

## Example Output

The following example shows the output from five tested companies:

AAPL

Company: Apple Inc.

Risk Score: 85

Risk Level: Low


MSFT

Company: Microsoft Corporation

Risk Score: 90

Risk Level: Low


NVDA

Company: NVIDIA Corporation

Risk Score: 70

Risk Level: Medium


GOOGL

Company: Alphabet Inc.

Risk Score: 90

Risk Level: Low


AMZN

Company: Amazon.com Inc.

Risk Score: 90

Risk Level: Low

---

## Ranking Results

Based on the calculated risk scores, the companies are ranked from lowest investment risk to highest investment risk.

| Rank | Company | Symbol | Risk Score | Risk Level |
|------|---------|--------|------------|------------|
| 1 | Microsoft Corporation | MSFT | 90 | Low Risk |
| 1 | Alphabet Inc. | GOOGL | 90 | Low Risk |
| 1 | Amazon.com Inc. | AMZN | 90 | Low Risk |
| 4 | Apple Inc. | AAPL | 85 | Low Risk |
| 5 | NVIDIA Corporation | NVDA | 70 | Medium Risk |

### Ranking Interpretation

Companies with higher risk scores receive better rankings because they demonstrate lower overall investment risk.

### Ranking Interpretation

Companies with higher risk scores receive better rankings because they demonstrate lower overall investment risk.

MSFT, GOOGL, and AMZN receive the highest rankings with risk scores of 90. These companies show relatively lower risk in this model based on the selected financial indicators.

AAPL is also classified as Low Risk, but it receives a slightly lower score because of moderate volatility and valuation-related risk flags.

NVDA receives the lowest ranking among the five companies and is classified as Medium Risk. Its lower score is mainly driven by higher stock volatility and valuation-related risk.

## Risk Flags

The tool also identifies important risk flags that may require additional research.

Risk flags help users understand why a company may have a higher risk score or lower ranking.

The main risk flags include:

- Missing financial data
- High stock volatility
- High P/E ratio
- Lower profitability
- Unusual or incomplete market data

### Example Risk Flags

| Company | Symbol | Risk Flag | Explanation |
|---------|--------|-----------|-------------|
| Apple Inc. | AAPL | Moderate volatility and valuation risk | AAPL is still classified as Low Risk, but moderate volatility and valuation risk reduce its score slightly. |
| Microsoft Corporation | MSFT | Low overall risk | MSFT receives one of the highest scores and is classified as Low Risk. |
| NVIDIA Corporation | NVDA | High volatility and valuation risk | NVDA receives a Medium Risk classification because higher volatility and valuation risk increase uncertainty. |
| Alphabet Inc. | GOOGL | Low overall risk | GOOGL receives a high score because the model does not detect major risk concerns. |
| Amazon.com Inc. | AMZN | Low overall risk | AMZN receives a high score and is classified as Low Risk in the current screening results. |

## Decision-Support Summary

The tool provides a short decision-support summary for each company. These summaries help users understand the strengths, weaknesses, and major risk indicators behind each score.

### Apple Inc. (AAPL)

Apple receives a Low Risk classification. The company has strong financial stability, a large market position, and relatively stable business performance. The main area for further review is whether future growth can continue to support its valuation.

### Microsoft Corporation (MSFT)

Microsoft receives a Low Risk classification. The company shows strong business stability, large market capitalization, and diversified revenue sources. Its risk profile is relatively low, although valuation should still be monitored.

### NVIDIA Corporation (NVDA)

NVIDIA receives a Medium Risk classification. The company has strong growth potential, but it also shows higher uncertainty because of valuation risk and market volatility. Investors may need to further investigate whether the growth outlook justifies the risk.

### Alphabet Inc. (GOOGL)

Alphabet receives a Low Risk classification. The company has strong financial performance, large market capitalization, and stable business fundamentals. Its high score suggests lower relative investment risk in this model.

### Amazon.com Inc. (AMZN)

Amazon receives a Low Risk classification. The company has strong market presence and diversified business segments. The model does not identify major risk concerns, but profitability and long-term margin trends should still be reviewed.

---

## Methodology

This section explains the data sources, calculations, assumptions, limitations, and update frequency used in this investment screening tool.

### Data Sources

The tool uses Yahoo Finance data through the `yfinance` Python package.

The data includes company information, current stock prices, market capitalization, valuation metrics, profitability indicators, and historical price data.

### Calculations

The tool collects financial metrics for each company and calculates a risk score.

The risk score starts from 100 points.

The score is adjusted based on:

- Stock volatility
- P/E ratio
- Profitability indicators
- Missing or incomplete financial data

A higher score represents lower investment risk.

### Assumptions

This model assumes that higher volatility indicates higher market risk.

It also assumes that higher valuation ratios, such as a high P/E ratio, may increase investment uncertainty.

The model is designed as a simplified investment screening framework and is not intended to replace professional financial analysis.

### Limitations

The tool depends on data availability from Yahoo Finance.

Some companies may have missing or incomplete financial metrics.

The model does not include all possible risk factors, such as macroeconomic conditions, interest rates, industry competition, management quality, or geopolitical risk.

The risk score should be used as a starting point for further research, not as a final investment recommendation.

### Update Frequency

The data is updated each time the program is run.

Because the tool fetches live financial data from Yahoo Finance, results may change over time as market prices and company metrics update.

## Project Structure

investment-risk-tool/

├── main.py

├── data_fetcher.py

├── risk_scoring.py

├── screening.py

├── requirements.txt

└── README.md


---

## Installation

Create a virtual environment:

python -m venv venv


Activate the environment:

Mac/Linux:

source venv/bin/activate


Install required packages:

pip install -r requirements.txt


---

## How to Run

Run the investment risk scoring tool:

python main.py


The program will collect company data, calculate risk scores, and display the screening results.

---

## Technologies Used

- Python
- Yahoo Finance API
- yfinance
- NumPy
- Pandas

---

## Future Improvements

Future improvements may include:

- Adding more financial indicators
- Supporting more companies
- Improving risk scoring algorithms
- Adding data visualization dashboards
- Integrating additional financial data sources
