# Finance API Project

## Overview

This project collects financial and economic data from:
- FRED
- Yahoo Finance
- Alpha Vantage

The raw API responses are transformed into a standardized JSON schema and exported into JSON and CSV formats.

## Project Structure

finance-api-project/
│
├── main.py
├── normalizer.py
├── snapshot.py
├── financial_snapshot.json
├── financial_snapshot.csv
├── requirements.txt
└── .env (not uploaded)

## Setup

1. Create virtual environment

2. Install dependencies

pip install -r requirements.txt

3. Create .env file

Add API keys:

FRED_API_KEY=
ALPHA_VANTAGE_API_KEY=

## Run

python snapshot.py

## Output

The program generates:
- financial_snapshot.json
- financial_snapshot.csv

## Normalization Approach

...

## Future Improvements

...
