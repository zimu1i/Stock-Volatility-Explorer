# 📊Stock Volatility Explorer
An interactive Streamlit web application that allows users to explore, compare, and interpret the historical volatility and performance of major U.S. stocks.
Built with Python, real-time market data, and an intuitive UI designed for both beginners and finance enthusiasts.

## Project Motivation 
Volatility is a key measure of financial risk, it helps investors to clarify risk when picking stocks. While some stocks are inherently volatile, others become risky only during periods. 

## Features

### 🔍 **Stock selection**
- Choose from 20+ popular stocks across technology, finance, consumer, crypto, healthcare, and ETFs
- Compare multiple tickers side-by-side

### 📈 **Data Visualization**
- Historical price charts (Price data retrieved using yfinance)
- Relative performance chart (normalized to base = 100)
- Annualized volatility table for quantitative comparison

### 🧠 **Volatility Insights**
- Automatically identifies:
  - 📈 Most volatile stock
  - 📉 Least volatile stock
- Provides contextual explanations based on:
  - Industry characteristics
  - Business models
  - Market sentiment
  - Macroeconomic factors
    
### 🔄 **Real-Time Updates**
- Optional auto-refresh every 60 seconds
- Cached computations for fast performance

### 📖 **Built-In User Guide**
- Step-by-step instructions directly inside the app
- Designed to be intuitive even for users with limited finance background

### 🛠️Tools Used
- Python
- Streamlit
- Pandas
- yfinance
- Matplotlib (via Streamlit charts)
- streamlit-autorefresh

## 📦 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/stock-volatility-explorer.git
cd stock-volatility-explorer
```
### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
### 3️⃣ Run the App
```bash
streamlit run app.py
```
The app will open automatically in your browser!

## 📊 Available Stock Universe

### *Includes (More to be added...):*

AAPL, MSFT, TSLA, NVDA, AMD, META, AMZN, JPM, SPY, GLD, SHOP, PLTR, RKLB, LLY, HOOD, BABA, INTC, AVGO, IREN, SBUX, ...

## 📌 Future Improvements
- Add rolling volatility windows
- Sector-level volatility comparison
- Exportable reports (CSV / PDF)
- Correlation matrix & heatmaps
- Options-implied volatility integration


