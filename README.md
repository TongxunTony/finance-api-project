# Finance API Project

## Overview

This project builds a financial data pipeline that collects and processes financial and economic data from multiple APIs.

The project uses:

- FRED API for GDP and CPI economic data
- Yahoo Finance API for stock market data
- Alpha Vantage API for financial data testing

The collected data is standardized and exported into JSON and CSV formats.

## Project Structure

- main.py
- snapshot.py
- normalizer.py
- requirements.txt
- financial_snapshot.json
- financial_snapshot.csv

## Features

- Connects to multiple financial data APIs
- Retrieves stock and economic indicators
- Stores API keys securely using environment variables
- Normalizes data into a consistent format
- Generates JSON and CSV financial snapshots

## Setup

Create a virtual environment:

python -m venv venv

Activate the environment:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt


Create a `.env` file:

FRED_API_KEY=your_key

ALPHA_VANTAGE_API_KEY=your_key


## Run

Run the project:

python snapshot.py


The program will generate:

- financial_snapshot.json
- financial_snapshot.csv


## Technologies Used

- Python
- FRED API
- Yahoo Finance API
- Alpha Vantage API
- pandas
- yfinance
- fredapi
- python-dotenv


## Future Improvements

Future improvements include adding more financial data sources, automating data collection, and applying machine learning methods for financial analysis.
