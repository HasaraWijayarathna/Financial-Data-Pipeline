from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
from datetime import datetime

# MongoDB connection string - REPLACE <db_password> with your actual password
MONGO_URI = "mongodb+srv://hasara2002_db_user:OsiHassa123!@cluster0.lze3yit.mongodb.net/?appName=Cluster0"

def connect_to_mongodb():
    """Connect to MongoDB Atlas"""
    try:
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def load_data_to_mongodb(client, ticker, data_path='data/processed'):
    """Load processed stock data to MongoDB"""
    db = client['financial_data']
    collection = db['stock_prices']
    
    # Read processed data
    df = pd.read_csv(f'{data_path}/{ticker}_processed.csv')
    
    # Convert to dictionary format
    records = df.to_dict('records')
    
    # Add metadata
    for record in records:
        record['ticker'] = ticker
        record['uploaded_at'] = datetime.now()
    
    # Insert into MongoDB
    result = collection.insert_many(records)
    print(f"Inserted {len(result.inserted_ids)} records for {ticker}")
    
    return len(result.inserted_ids)

def load_all_stocks():
    """Load all stock data to MongoDB"""
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    
    client = connect_to_mongodb()
    if not client:
        return
    
    total_records = 0
    for ticker in tickers:
        print(f"\nLoading {ticker}...")
        count = load_data_to_mongodb(client, ticker)
        total_records += count
    
    print(f"\nTotal records loaded: {total_records}")
    
    client.close()

if __name__ == "__main__":
    load_all_stocks()