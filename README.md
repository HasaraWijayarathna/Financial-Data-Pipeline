# Financial Data Pipeline - Automated ETL & AI-Powered Insights

![Python](https://img.shields.io/badge/Python-3.11-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📊 Project Overview

Automated financial data pipeline that extracts real-time stock data from Yahoo Finance API, calculates advanced financial metrics, generates AI-powered market insights, and stores everything in MongoDB Atlas cloud database. The system includes interactive Power BI dashboards for comprehensive financial analysis and risk assessment.

**Key Achievement:** 60-second end-to-end execution time with complete error handling and logging.

---

## 🎯 Business Problem

Financial analysts need:
- **Real-time stock data** from reliable sources
- **Advanced metrics** (Sharpe ratio, max drawdown, volatility) calculated automatically
- **AI-powered insights** to identify market trends and risks
- **Cloud storage** for historical tracking and analysis
- **Visual dashboards** for executive reporting

**Solution:** Fully automated ETL pipeline with cloud integration and intelligent analytics.

---

## 🚀 Key Features

### 1. **Data Extraction**
- Yahoo Finance API integration
- 5-year historical data retrieval
- 10 major stocks tracked (AAPL, MSFT, GOOGL, AMZN, TSLA, etc.)
- Automatic retry logic and error handling

### 2. **Advanced Financial Metrics**
- **Sharpe Ratio** - Risk-adjusted return calculation
- **Maximum Drawdown** - Largest peak-to-trough decline
- **Volatility** - Standard deviation of returns
- **Cumulative Returns** - Total performance tracking
- **Daily Returns** - Day-over-day changes

### 3. **AI-Powered Insights** (OpenAI API)
- Market trend analysis
- Risk assessment
- Investment recommendations
- Fallback to simulated insights if API unavailable

### 4. **Cloud Data Storage**
- MongoDB Atlas cloud database
- Structured document storage
- Historical data retention
- Scalable NoSQL architecture

### 5. **Interactive Power BI Dashboard**
- Executive summary with KPIs
- Stock performance comparison
- Risk-return scatter plots
- Time series trend analysis
- Detailed metric breakdowns

---

## 📊 Power BI Dashboard Visualizations

### **Correlation Heatmap**
![Correlation Analysis](screenshots/correlation_heatmap.png)
*Correlation matrix showing relationships between different stocks*

### **Price Comparison**
![Price Trends](screenshots/price_comparison.png)
*Historical price movements across analyzed stocks*

### **Returns Comparison**
![Returns Analysis](screenshots/returns_comparison.png)
*Comparative analysis of returns across different securities*

### **Risk-Return Profile**
![Risk-Return](screenshots/risk_return_profile.png)
*Risk-return scatter plot identifying optimal investment opportunities*

### **Risk vs Returns**
![Risk Returns](screenshots/risk_returns.png)
*Detailed risk assessment against expected returns*

### **Stock Overview**
![Stock Overview](screenshots/stock_overview.png)
*Comprehensive overview of all tracked stocks with key metrics*

### **Technical Analysis**
![Technical Analysis](screenshots/technical_analysis.png)
*Moving averages, trend indicators, and technical metrics*

### **Volatility Comparison**
![Volatility](screenshots/volatility_comparison.png)
*Volatility analysis across different stocks and time periods*

### **Moving Averages**
![Moving Averages](screenshots/moving_averages.png)
*50-day and 200-day moving average analysis*

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.11 |
| **Data Processing** | pandas, NumPy |
| **API Integration** | yfinance, OpenAI API |
| **Database** | MongoDB Atlas (Cloud NoSQL) |
| **Visualization** | Power BI Desktop, matplotlib, seaborn |
| **Version Control** | Git/GitHub |

---

## 📁 Project Structure
```
Financial-Data-Pipeline/
├── dashboards/
│   └── financial_dashboard.pbix       # Power BI dashboard file
├── screenshots/
│   ├── correlation_heatmap.png
│   ├── financial_dashboard.png
│   ├── moving_averages.png
│   ├── price_comparison.png
│   ├── returns_comparison.png
│   ├── risk_return_profile.png
│   ├── risk_returns.png
│   ├── stock_overview.png
│   ├── technical_analysis.png
│   └── volatility_comparison.png
├── data/
│   ├── raw/                           # Raw stock data
│   └── processed/                     # Calculated metrics
├── notebooks/                          # Jupyter notebooks
├── scripts/                            # Python scripts
├── sql/                                # SQL queries
├── reports/                            # Analysis reports
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔧 Installation & Setup

### **1. Clone Repository**
```bash
git clone https://github.com/HasaraWijayarathna/Financial-Data-Pipeline.git
cd Financial-Data-Pipeline
```

### **2. Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run Analysis**
```bash
python scripts/pipeline.py
```

---

## 📈 Key Metrics Calculated

### **1. Sharpe Ratio**
Measures risk-adjusted return:
```
Sharpe Ratio = (Mean Return - Risk-Free Rate) / Standard Deviation
```
**Interpretation:** Higher is better. > 1.0 is good, > 2.0 is excellent.

### **2. Maximum Drawdown**
Largest peak-to-trough decline:
```
Max Drawdown = (Trough Value - Peak Value) / Peak Value
```
**Interpretation:** Closer to 0 is better (less risk).

### **3. Volatility**
Annual standard deviation of returns:
```
Volatility = Daily Returns Std Dev × √252
```
**Interpretation:** Lower volatility = more stable investment.

### **4. Cumulative Returns**
Total return over investment period:
```
Cumulative Return = (Final Price / Initial Price) - 1
```

---

## 🎓 Skills Demonstrated

### **Data Engineering**
✅ API integration and data extraction  
✅ ETL pipeline design and orchestration  
✅ Error handling and logging  
✅ Data validation and cleaning  

### **Cloud Technologies**
✅ MongoDB Atlas (NoSQL cloud database)  
✅ Connection pooling and optimization  
✅ Document-based data modeling  

### **Financial Analysis**
✅ Advanced metric calculation (Sharpe, drawdown, volatility)  
✅ Risk-return analysis  
✅ Portfolio performance evaluation  

### **AI Integration**
✅ OpenAI API implementation  
✅ Prompt engineering for financial insights  
✅ Fallback mechanism design  

### **Data Visualization**
✅ Power BI dashboard development  
✅ Interactive visualizations  
✅ Executive reporting  

---

## 📊 Business Impact

| Metric | Value | Impact |
|--------|-------|--------|
| **Execution Time** | 60 seconds | Real-time analysis capability |
| **Data Points** | 12,500+ | 5 years × 10 stocks × 250 trading days |
| **Metrics Calculated** | 5 per stock | Comprehensive risk assessment |
| **AI Insights** | 10 per run | Automated decision support |
| **Cloud Storage** | Unlimited | Historical tracking enabled |

**ROI:** Replaces 2-3 hours of manual analysis with 60-second automated process.

---

## 🔮 Future Enhancements

- [ ] Real-time streaming data (WebSocket integration)
- [ ] Portfolio optimization algorithms
- [ ] Predictive modeling (LSTM for price forecasting)
- [ ] Email alerting system for threshold breaches
- [ ] Multi-asset class support (bonds, crypto, commodities)
- [ ] Backtesting framework for trading strategies

---

## 👨‍💻 Author

**Hasara Wijayarathna**  
Data Science & Business Analytics Student  
📧 Email: hasara2002@gmail.com  
💼 GitHub: [@HasaraWijayarathna](https://github.com/HasaraWijayarathna)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- Yahoo Finance for financial data API
- MongoDB Atlas for cloud database hosting
- OpenAI for AI-powered insights capability
- Power BI for visualization platform

---

**⭐ If you found this project helpful, please consider giving it a star!**
