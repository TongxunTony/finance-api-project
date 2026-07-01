# Finance API Project

## Overview

This project demonstrates how to connect to multiple financial data APIs using Python.

The program retrieves data from:

- FRED (Federal Reserve Economic Data)
- Yahoo Finance
- Alpha Vantage

## Features

- Connects to three different APIs
- Loads API keys securely from a `.env` file
- Returns financial and economic data in JSON format
- Uses Python and the `requests` library

## Project Structure

```
finance-api-project/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not uploaded to GitHub)
```

## Requirements

Install the required packages with:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Notes

The `.env` file is excluded from GitHub to protect API keys.
