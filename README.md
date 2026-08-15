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

Risk Score: 85

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