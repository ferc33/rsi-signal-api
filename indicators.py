import pandas as pd
import ta

def calculate_macd(data: pd.DataFrame):
    macd = ta.trend.MACD(data['Close'])
    data['MACD'] = macd.macd_diff()
    signal = "Buy" if data['MACD'].iloc[-1] > 0 else "Sell"
    return signal

def calculate_rsi(data: pd.DataFrame):
    rsi = ta.momentum.RSIIndicator(data['Close'])
    data['RSI'] = rsi.rsi()
    signal = "Buy" if data['RSI'].iloc[-1] < 30 else "Sell" if data['RSI'].iloc[-1] > 70 else "Hold"
    return signal

