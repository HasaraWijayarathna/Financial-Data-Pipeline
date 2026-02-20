import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance
    
    Parameters:
    tickers (list): List of stock ticker symbols
    start_date (str): Start date in YYYY-MM-DD format
    end_date (str): End date in YYYY-MM-DD format
    
    Returns:
    dict: Dictionary of dataframes for each ticker
    """
    stock_data = {}
    
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        try:
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)
            stock_data[ticker] = data
            print(f"Successfully fetched {len(data)} records for {ticker}")
        except Exception as e:
            print(f"Error fetching {ticker}: {str(e)}")
    
    return stock_data

def save_raw_data(stock_data, output_dir='../data/raw'):
    """Save raw stock data to CSV files"""
    os.makedirs(output_dir, exist_ok=True)
    
    for ticker, data in stock_data.items():
        # Reset index to make Date a column
        data_reset = data.reset_index()
        filepath = os.path.join(output_dir, f"{ticker}_raw.csv")
        data_reset.to_csv(filepath, index=False)
        print(f"Saved {ticker} data to {filepath}")

if __name__ == "__main__":
    # Define stock tickers to analyze
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    
    # Define date range (last 2 years)
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=730)).strftime('%Y-%m-%d')
    
    print(f"Fetching stock data from {start_date} to {end_date}")
    print(f"Tickers: {tickers}\n")
    
    # Fetch data
    stock_data = fetch_stock_data(tickers, start_date, end_date)
    
    # Save to CSV
    save_raw_data(stock_data)
    
    print("\nData extraction complete!")