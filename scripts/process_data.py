import pandas as pd
import numpy as np
import os

def load_stock_data(ticker, data_dir='data/raw'):
    """Load raw stock data from CSV"""
    filepath = os.path.join(data_dir, f"{ticker}_raw.csv")
    df = pd.read_csv(filepath, index_col=0)
    
    # Convert index to datetime
    df.index = pd.to_datetime(df.index)
    df.index.name = 'Date'
    
    # Convert numeric columns
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

def calculate_technical_indicators(df):
    """Calculate technical indicators for stock analysis"""
    # Daily returns
    df['Daily_Return'] = df['Close'].pct_change(fill_method=None)
    
    # Moving averages
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    df['MA_200'] = df['Close'].rolling(window=200).mean()
    
    # Volatility
    df['Volatility'] = df['Daily_Return'].rolling(window=20).std()
    
    # Momentum
    df['Momentum'] = df['Close'] - df['Close'].shift(10)
    
    # Volume moving average
    df['Volume_MA'] = df['Volume'].rolling(window=20).mean()
    
    return df

def add_features(df, ticker):
    """Add additional features"""
    df['Ticker'] = ticker
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Day_of_Week'] = df.index.dayofweek
    
    return df

def process_all_stocks(tickers):
    """Process data for all tickers"""
    processed_data = {}
    
    for ticker in tickers:
        print(f"Processing {ticker}...")
        
        df = load_stock_data(ticker)
        df = calculate_technical_indicators(df)
        df = add_features(df, ticker)
        df = df.dropna()
        
        processed_data[ticker] = df
        print(f"Processed {len(df)} records for {ticker}")
    
    return processed_data

def save_processed_data(processed_data, output_dir='data/processed'):
    """Save processed data"""
    os.makedirs(output_dir, exist_ok=True)
    
    for ticker, df in processed_data.items():
        filepath = os.path.join(output_dir, f"{ticker}_processed.csv")
        df.to_csv(filepath)
        print(f"Saved {ticker}")
    
    combined_df = pd.concat(processed_data.values())
    combined_df.to_csv(os.path.join(output_dir, 'all_stocks_combined.csv'))
    print(f"\nSaved combined dataset: {len(combined_df)} records")

if __name__ == "__main__":
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    print("Processing stock data...\n")
    processed_data = process_all_stocks(tickers)
    save_processed_data(processed_data)
    print("\nComplete!")