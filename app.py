from streamlit_autorefresh import st_autorefresh  # pyright: ignore[reportMissingImports]

import streamlit as st  # pyright: ignore[reportMissingImports]
st.title("Stock Volatility Explorer")
st.write("This app allows you to explore the volatility of different stocks.")

# User Guide Section
with st.expander("📖 How to Use This App", expanded=True):
    st.markdown("""
    ### Getting Started
    
    1. **Select Stock Tickers**: Use the sidebar on the left to choose one or more stock tickers from the dropdown menu. 
       - Choose from 20+ popular stocks across various sectors
       - You can select multiple tickers to compare their volatility side-by-side
    
    2. **Enable Auto-Refresh** (Optional): Check the "Enable auto-refresh" box in the sidebar to automatically update the data every 60 seconds. 
       - This is useful for monitoring real-time changes in stock volatility
       - Uncheck it if you prefer manual refreshes
    
    3. **Adjust Start Date** (Optional): Use the date picker in the sidebar to change the historical data range (default: January 1, 2020)
    
    ### Understanding the Results
    
    Once you've selected your tickers, the app will display:
    
    - **Recent Price Data**: A table showing the latest closing prices for your selected stocks
    
    - **Stock Prices Chart**: A line chart displaying the historical closing prices for all selected stocks over time
    
    - **Relative Performance Chart**: Shows how each stock has performed relative to its starting value (normalized to 100), making it easy to compare performance regardless of absolute price differences
    
    - **Annualized Volatility Table**: Displays the calculated volatility metric for each stock, which measures the degree of variation in stock prices over time
    
    - **Volatility Insights**: The app automatically identifies:
      - The stock with the **highest volatility** and provides context about why it might be volatile
      - The stock with the **lowest volatility** and explains factors contributing to its stability
    
    ### Tips
    
    - Select at least one ticker to begin the analysis
    - Compare different sectors (e.g., tech stocks vs. financial stocks) to see how volatility varies
    - Use the relative performance chart to identify which stocks have outperformed others over the selected time period
    - Higher volatility indicates greater price swings, which can mean both higher risk and potential for higher returns
    """)

st.sidebar.header("Controls")

# Option to enable/disable auto-refresh
auto_refresh = st.sidebar.checkbox("Enable auto-refresh (every 60s)", value=True)
if auto_refresh:
    st_autorefresh(interval=60 * 1000, key="refresh")

# Default tickers
default_tickers = ["AAPL", "MSFT", "TSLA", "JPM", "SPY", "NVDA", "AMD", "SBUX", "BABA", "INTC", "HOOD", "AVGO", "IREN", "META", "SHOP", "RKLB", "LLY", "GLD", "AMZN", "PLTR"]

# Multiselect for stock tickers
selected_tickers = st.sidebar.multiselect(
    "Select Stock Tickers",
    options=default_tickers,
    default=[],
    help="Choose one or more stock tickers to analyze"
)

# Check if at least one ticker is selected
if len(selected_tickers) == 0:
    st.warning("⚠️ Please select at least one stock ticker to proceed with the analysis.")

import yfinance as yf  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from datetime import datetime

@st.cache_data(ttl=60)  # Cache expires after 60 seconds for real-time updates
def load_data(tickers_tuple, start_date):
    # Convert tuple back to list for yfinance
    tickers = list(tickers_tuple)
    data = yf.download(tickers, start=start_date, progress=False)["Close"]
    return data

@st.cache_data(ttl=60)
def compute_metrics(prices):
    """Cache expensive computations"""
    normalized = prices / prices.iloc[0] * 100
    returns = prices.pct_change()
    volatility = returns.std() * (252 ** 0.5)
    return normalized, returns, volatility

def get_volatility_insight(ticker, is_highest=True):
    """Generate insights about why a stock has high or low volatility"""
    insights = {
        "AAPL": {
            "high": "Apple's volatility is typically moderate due to its large market cap and diversified product portfolio. Higher volatility may stem from product launch cycles, supply chain disruptions, or broader tech sector sentiment.",
            "low": "Apple maintains relatively stable volatility as a mega-cap tech company with strong brand loyalty, recurring revenue streams, and a massive cash position providing financial stability."
        },
        "MSFT": {
            "high": "Microsoft's volatility can increase due to enterprise contract cycles, cloud computing competition, or regulatory concerns. Recent volatility may reflect shifting market dynamics in the tech sector.",
            "low": "Microsoft demonstrates low volatility thanks to its diversified business model (software, cloud, gaming), strong enterprise relationships, and consistent dividend payments that attract stable investors."
        },
        # ... (all other tickers remain unchanged)
    }
    
    key = "high" if is_highest else "low"
    return insights.get(ticker, {}).get(key, f"{ticker} volatility is influenced by market conditions, sector dynamics, and company-specific factors.")

if len(selected_tickers) > 0:
    start_date = st.sidebar.date_input("Start date", value=pd.to_datetime("2020-01-01"))
    
    # Load and cache data
    prices = load_data(tuple(sorted(selected_tickers)), start_date=start_date)  # Sort for consistent cache key
    
    # Compute metrics with caching
    normalized, returns, volatility = compute_metrics(prices)
    
    # Display last update time
    st.caption(f"🔄 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    st.write(prices.tail())

    st.subheader("Stock Prices")
    st.line_chart(prices)

    st.subheader("Relative Performance (Base = 100)")
    st.line_chart(normalized)

    st.subheader("Annualized Volatility")
    st.dataframe(volatility.to_frame("Volatility"))

    # Find highest and lowest volatility stocks
    highest_vol_ticker = volatility.idxmax()
    lowest_vol_ticker = volatility.idxmin()
    
    # Combine value + insight in one display per ticker
    st.success(f"📈 Highest volatility: {highest_vol_ticker} ({volatility[highest_vol_ticker]:.2%})\n\n💡 Insight: {get_volatility_insight(highest_vol_ticker, is_highest=True)}")
    st.error(f"📉 Lowest volatility: {lowest_vol_ticker} ({volatility[lowest_vol_ticker]:.2%})\n\n💡 Insight: {get_volatility_insight(lowest_vol_ticker, is_highest=False)}")
