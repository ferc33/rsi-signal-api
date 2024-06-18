from apscheduler.schedulers.background import BackgroundScheduler
from utils import fetch_gold_data
from indicators import calculate_macd, calculate_rsi
from telegram_utils import send_telegram_message
import time

def send_trading_signals():
    data = fetch_gold_data()
    last_close = data['Close'].iloc[-1]
    prev_close = data['Close'].iloc[-2]

    macd_signal = calculate_macd(data)
    rsi_signal = calculate_rsi(data)

    if macd_signal == "Buy" or rsi_signal == "Buy":
        if last_close > prev_close:
            send_telegram_message(f"Buy Signal: Gold price is increasing ({last_close})")

    if macd_signal == "Sell" or rsi_signal == "Sell":
        if last_close < prev_close:
            send_telegram_message(f"Sell Signal: Gold price is decreasing ({last_close})")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_trading_signals, 'interval', minutes=5)
    scheduler.start()

    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

if __name__ == "__main__":
    start_scheduler()