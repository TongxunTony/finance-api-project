Finance API Project
Overview

This project builds a financial data pipeline that collects and processes financial and economic data from multiple APIs.

The project uses:

FRED API for macroeconomic indicators such as GDP and CPI
Yahoo Finance API for stock market data such as Apple (AAPL) price information
Alpha Vantage API for additional financial data testing

The collected data is combined, standardized, and exported into JSON and CSV formats for further analysis.

Project Structure

finance-api-project/

├── main.py
├── snapshot.py
├── normalizer.py
├── requirements.txt
├── README.md
├── financial_snapshot.json
└── financial_snapshot.csv

Features
Connects to multiple financial data APIs
Retrieves stock market and economic indicators
Uses environment variables to securely store API keys
Normalizes data into a consistent structure
Exports processed financial snapshots as JSON and CSV files
Setup
Create a virtual environment:

python -m venv venv

Activate the environment:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a .env file and add API keys:

FRED_API_KEY=your_key
ALPHA_VANTAGE_API_KEY=your_key

Run

Run the project using:

python snapshot.py

The program will collect financial data and generate:

financial_snapshot.json
financial_snapshot.csv
Technologies Used
Python
FRED API
Yahoo Finance API
Alpha Vantage API
pandas
yfinance
fredapi
python-dotenv
Future Improvements

Future improvements include adding more financial data sources, automating data collection, and applying machine learning models for financial analysis.
