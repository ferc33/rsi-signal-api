import yfinance as yf
import logging

logging.basicConfig(level=logging.INFO)
def fetch_gold_data(ticker="GC=F", period="1mo", interval="1h"):
    gold = yf.Ticker(ticker)
    data = gold.history(period=period, interval=interval)
    return data
    
async def send_telegram_message(message: str):
    try:
        logging.info(f"Enviando mensaje: {message}")
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="HOLA FER")
    except Exception as e:
        logging.error(f"Error al enviar mensaje: {e}")