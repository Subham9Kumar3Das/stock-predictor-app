import yfinance as yf
import pandas as pd

def get_stock_data(ticker, start='2015-01-01', end='2024-12-31'):
    data = yf.download(ticker, start=start, end=end)
    return data[['Close']]
