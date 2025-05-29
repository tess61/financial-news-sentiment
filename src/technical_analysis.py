import pandas as pd
import talib
import os
import matplotlib.pyplot as plt

def load_stock_data(filepath):
    """Loads a CSV into a cleaned DataFrame."""
    df = pd.read_csv(filepath, parse_dates=["Date"])
    df = df.sort_values("Date").set_index("Date")
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    return df

def apply_technical_indicators(df):
    """Adds TA-Lib indicators to the DataFrame."""
    df["SMA_20"] = talib.SMA(df["Close"], timeperiod=20)
    df["SMA_50"] = talib.SMA(df["Close"], timeperiod=50)
    df["RSI"] = talib.RSI(df["Close"], timeperiod=14)
    df["MACD"], df["MACD_signal"], df["MACD_hist"] = talib.MACD(df["Close"])
    return df

def plot_price_with_indicators(df, ticker):
    """Visualizes Close price and indicators."""
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df["Close"], label="Close Price", color="black")
    plt.plot(df.index, df["SMA_20"], label="SMA 20", linestyle="--", color="blue")
    plt.plot(df.index, df["SMA_50"], label="SMA 50", linestyle="--", color="orange")
    plt.title(f"{ticker} Closing Price & Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()