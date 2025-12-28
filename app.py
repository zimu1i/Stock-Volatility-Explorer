from streamlit_autorefresh import st_autorefresh  # pyright: ignore[reportMissingImports]

st_autorefresh(interval=60 * 1000, key="datarefresh")

import streamlit as st
st.title("Stock Volatility Explorer")
st.write("This app allows you to explore the volatility of different stocks.")

st.sidebar.header("Controls")

# Default tickers
default_tickers = ["AAPL", "MSFT", "TSLA", "JPM", "SPY"]

# Multiselect for stock tickers
selected_tickers = st.sidebar.multiselect(
    "Select Stock Tickers",
    options=default_tickers,
    default=default_tickers,
    help="Choose one or more stock tickers to analyze"
)

# Check if at least one ticker is selected
if len(selected_tickers) == 0:
    st.warning("⚠️ Please select at least one stock ticker to proceed with the analysis.")
import yfinance as yf
import pandas as pd
from datetime import datetime

@st.cache_data(ttl=60)  # Cache expires after 60 seconds for real-time updates
def load_data(tickers):
    data = yf.download(tickers, start="2020-01-01", progress=False)["Close"]
    return data

if len(selected_tickers) > 0:
    prices = load_data(selected_tickers)
    
    # Display last update time
    st.caption(f"🔄 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    st.write(prices.tail())

    st.subheader("Stock Prices")
    st.line_chart(prices)

    normalized = prices / prices.iloc[0]*100

    st.subheader("Relative Performance (Base = 100)")
    st.line_chart(normalized)

    returns = prices.pct_change()

    volatility = returns.std() * (252 ** 0.5)

    st.subheader("Annualized Volatility")
    st.dataframe(volatility.rename("Volatility"))

    start_date = st.sidebar.date_input("Start date", value=pd.to_datetime("2020-01-01"))

    best = normalized.iloc[-1].idxmax()
    st.success(f"📈 Best performer: {best}")

    worst = normalized.iloc[-1].idxmin()
    st.error(f"📉 Worst performer: {worst}")