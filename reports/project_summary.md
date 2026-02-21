@"
# Financial Data Pipeline - Project Summary

## Overview
Automated ETL pipeline for financial market analysis, demonstrating end-to-end data engineering and analysis skills.

## Technical Implementation

### Data Extraction
- Yahoo Finance API integration
- Real-time stock data for 5 major tech companies (AAPL, GOOGL, MSFT, AMZN, TSLA)
- 501 trading days per stock (2 years of data)

### Data Processing
- Calculated technical indicators: Moving Averages (20, 50, 200-day), Volatility, Momentum
- Daily returns and volume analysis
- Time-series feature engineering

### Data Storage
- MongoDB Atlas cloud database
- 1,510 processed records stored
- Structured NoSQL document format

### Analysis & Insights
- Stock price comparison and correlation analysis
- Volatility ranking: TSLA highest (0.0369), MSFT lowest (0.0145)
- Returns analysis: GOOGL +74.56%, MSFT -8.23%
- Moving average trading signals identified

## Key Findings

**Best Performer:** Google (GOOGL) - 74.56% return  
**Most Volatile:** Tesla (TSLA) - 3.69% average volatility  
**Correlation:** AAPL-GOOGL highly correlated (0.849) - diversification risk  

## Skills Demonstrated

- API integration (Yahoo Finance)
- ETL pipeline development
- Cloud database management (MongoDB Atlas)
- Technical indicator calculation
- Financial data analysis
- Data visualization
- Python automation

## Technologies Used

Python, pandas, NumPy, yfinance, pymongo, MongoDB Atlas, matplotlib, seaborn, Jupyter

## Author
Hasara Wijayarathna
"@ | Out-File -FilePath reports/project_summary.md -Encoding UTF8
