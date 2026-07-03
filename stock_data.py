from pathlib import Path
import pandas as pd
import yfinance as yf

root = Path("/stock_analyzer")
stock_file = root / "stock_data.py"

def get_stock_data(ticker):
    data = yf.download(ticker, start="2024-01-01", end="2025-01-01")
    return data

if __name__ == "__main__":
    df = get_stock_data("AAPL")
    print(df.head())