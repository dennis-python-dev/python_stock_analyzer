# Stock Market Analysis Tool

## Overview
This project is a Python-based stock market analysis tool that retrieves historical stock data using the yFinance API and performs basic financial analysis using Pandas.

It calculates technical indicators such as moving averages and generates simple trading signals based on trend behavior.

---

## Features
- Fetches real stock data using yFinance
- Calculates daily returns
- Computes moving averages (5-day and 20-day)
- Generates simple BUY / SELL / HOLD signals
- Exports analyzed data to CSV

---

## Technologies Used
- Python
- Pandas
- yFinance

---

## How It Works
1. Downloads historical stock data (AAPL by default)
2. Applies data transformations:
   - Moving averages
   - Signal generation
3. Displays latest analysis
4. Saves results to a CSV file

---

## Output Example
The script generates a file:
