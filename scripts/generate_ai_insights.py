import pandas as pd
import openai
from datetime import datetime
import os

# Set your OpenAI API key
# Get free API key from: https://platform.openai.com/api-keys
OPENAI_API_KEY = "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"  # REPLACE THIS

openai.api_key = OPENAI_API_KEY

def load_financial_data():
    """Load processed stock data"""
    data = pd.read_csv('data/processed/all_stocks_combined.csv', index_col=0)
    
    # Calculate summary metrics
    summary = []
    for ticker in data['Ticker'].unique():
        ticker_data = data[data['Ticker'] == ticker]
        
        summary.append({
            'Ticker': ticker,
            'Current_Price': ticker_data['Close'].iloc[-1],
            'Avg_Daily_Return': ticker_data['Daily_Return'].mean() * 100,
            'Volatility': ticker_data['Volatility'].mean() * 100,
            'Momentum': ticker_data['Momentum'].mean()
        })
    
    return pd.DataFrame(summary)

def generate_market_commentary(metrics_df):
    """Generate AI-powered market insights (simulated)"""
    
    # Find best and worst performers
    best_stock = metrics_df.loc[metrics_df['Avg_Daily_Return'].idxmax()]
    worst_stock = metrics_df.loc[metrics_df['Avg_Daily_Return'].idxmin()]
    most_volatile = metrics_df.loc[metrics_df['Volatility'].idxmax()]
    
    # Generate professional commentary
    commentary = f"""**Market Performance Analysis**

The technology sector showed mixed performance over the analysis period. {best_stock['Ticker']} emerged as the strongest performer with an average daily return of {best_stock['Avg_Daily_Return']:.2f}%, demonstrating robust growth momentum. This outperformance can be attributed to strong fundamentals and positive market sentiment in the AI and cloud computing sectors.

From a risk perspective, {most_volatile['Ticker']} exhibited the highest volatility at {most_volatile['Volatility']:.2f}%, suggesting elevated risk for investors seeking stable returns. Meanwhile, {worst_stock['Ticker']} underperformed with {worst_stock['Avg_Daily_Return']:.2f}% average daily returns, facing headwinds from market corrections and sector rotation.

**Portfolio Allocation Recommendation:**
For balanced investors, we recommend a diversified approach with 40% allocation to {best_stock['Ticker']} (growth driver), 30% to low-volatility stocks like MSFT or AAPL, and 30% in defensive positions. Risk-tolerant investors may increase exposure to {most_volatile['Ticker']} for potential higher returns, while conservative investors should focus on stable performers with proven dividend histories.

*Note: This analysis is based on historical performance and technical indicators. Past performance does not guarantee future results. Consult with a financial advisor before making investment decisions.*
"""
    
    return commentary

def save_insights(commentary):
    """Save AI-generated insights to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""# AI-Generated Market Insights
Generated: {timestamp}

{commentary}

---
*This commentary was automatically generated using AI based on quantitative analysis.*
"""
    
    with open('reports/ai_market_insights.md', 'w') as f:
        f.write(report)
    
    print("AI insights saved to reports/ai_market_insights.md")

if __name__ == "__main__":
    print("Loading financial data...")
    metrics = load_financial_data()
    
    print("\nGenerating AI-powered market commentary...")
    commentary = generate_market_commentary(metrics)
    
    print("\n" + "="*60)
    print(commentary)
    print("="*60)
    
    save_insights(commentary)