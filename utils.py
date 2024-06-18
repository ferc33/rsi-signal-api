import yfinance as yf

def fetch_gold_data(ticker="GC=F", period="1mo", interval="1h"):
    gold = yf.Ticker(ticker)
    data = gold.history(period=period, interval=interval)
    return data

