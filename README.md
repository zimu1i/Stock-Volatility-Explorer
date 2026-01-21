# Stock Volatility Explorer
An interactive web app that helps you explore and compare how much different stocks bounce around—and what that means for your investment decisions.

Built with Python and designed for everyone from curious beginners to seasoned investors.

## Why This Project?
Ever wonder why some stocks feel like a rollercoaster while others barely budge? Volatility tells you how much a stock's price swings up and down. Understanding this helps you pick investments that match your risk tolerance, whether you're looking for steady growth or chasing bigger (riskier) gains.

This tool makes volatility analysis simple and visual, so you don't need a finance degree to understand what's happening.

## What It Does

### Pick Your Stocks
Choose from 20+ popular stocks across tech, finance, healthcare, crypto, and more. Compare as many as you want side-by-side.

####  See the Story in Charts

Price History: Watch how stocks have moved over time
Relative Performance: See which stocks outpaced the others (normalized to 100 for easy comparison)
Volatility Rankings: Quick table showing which stocks are wild vs. calm

#### Get Real Insights
The app automatically highlights:

- Most volatile stock – and why it's so jumpy
- Least volatile stock – and what makes it stable

You'll get plain-English explanations based on industry trends, business models, and market conditions, no jargon overload!

#### Stay Current
- Optional auto-refresh every 60 seconds for live-ish data
- Smart caching so everything loads fast
    
#### Easy to Use
Built-in guide walks you through everything. No finance background needed.

## What's Under the Hood

- Python – the engine
- Streamlit – the slick interface
- yfinance – real market data
- Pandas – data wrangling
- Matplotlib – beautiful charts
- streamlit-autorefresh – keeps things current

## Get it Running!

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zimu1i/Stock-Volatility-Explorer
cd Stock-Volatility-Explorer
```
### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
### 3️⃣ Run the App
```bash
streamlit run app.py
```
Your browser should pop open automatically!

## Stocks You Can Explore
- Tech: AAPL, MSFT, TSLA, NVDA, AMD, META, AMZN, INTC, AVGO
- Finance: JPM, HOOD
- E-commerce: SHOP, BABA
- Healthcare: LLY
- Space: RKLB
- Defense/Tech: PLTR
- Crypto Mining: IREN
- Consumer: SBUX
- ETFs: SPY, GLD

## What's Next
- Rolling volatility windows – see how stability changes over time
- Sector comparisons – tech vs. finance vs. healthcare volatility
- Export reports – save your analysis as CSV or PDF
- Correlation heatmaps – see which stocks move together
- Options data – integrate implied volatility for deeper insights

## Disclaimer

This tool is built for learning and exploration. It shows you historical data and helps you understand patterns, but:
It's NOT financial advice. Markets are unpredictable. Past performance doesn't guarantee future results. Always do your own research or talk to a professional before making investment decisions.
Use this as a starting point, not the final word.
