from pathlib import Path
import pandas as pd
import yfinance as yf

root = Path("/home/kingwiz1/myspace/safezone/stock_analyzer")
stock_file = root / "analysis.py"

def get_stock_data(ticker):
    df = yf.download(ticker, start="2024-01-01", end="2025-01-01")
    return df

def analyzer(df):
    # Daily Return
    df["Daily_Return"] = df["Close"].pct_change()
    
    # Moving Averages
    df["MA_5"] = df["Close"].rolling(window=5).mean()
    df["MA_20"] = df["Close"].rolling(window=20).mean()
    
    # Simple signal
    df["Signal"] = "Hold"
    df.loc[df["MA_5"] > df["MA_20"], "Signal"] = "Buy"
    df.loc[df["MA_5"] < df["MA_20"], "Signal"] = "Sell"
    
    return df

if __name__ == "__main__":
    data = get_stock_data("AAPL")
    result = analyzer(data)
    
    print(result[["Close", "MA_5", "MA_20", "Signal"]].tail(10))
    
    result.to_csv("stock_analysis_results.csv")
    print("\nResults saved to stock_analysis_results.csv")