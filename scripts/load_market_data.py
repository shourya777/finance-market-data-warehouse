import yfinance as yf
import pandas as pd

# Choose assets (Bloomberg-style tickers)
tickers = ["AAPL", "MSFT", "JPM", "GS"]

# Download market data
data = yf.download(
    tickers,
    start="2023-01-01",
    end="2024-01-01"
)

# Reshape dataframe
data = data["Close"].reset_index()
data = data.melt(id_vars=["Date"],
                 var_name="ticker",
                 value_name="close_price")

# Save locally
data.to_csv("data/market_prices.csv", index=False)

print("Market data saved successfully.")
