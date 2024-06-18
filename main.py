from fastapi import FastAPI
from utils import fetch_gold_data
from indicators import calculate_macd, calculate_rsi
from telegram_utils import send_telegram_message

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gold Trading API"}

@app.get("/signal/")
async def get_trading_signal():
    data = fetch_gold_data()
    macd_signal = calculate_macd(data)
    rsi_signal = calculate_rsi(data)
    
    signal = {
        "MACD": macd_signal,
        "RSI": rsi_signal,
    }

    # Enviar mensaje de Telegram si se cumple una condición
    if macd_signal == "Buy" or macd_signal == "Sell":
        await send_telegram_message(f"MACD Signal: {macd_signal}")
    if rsi_signal == "Buy" or rsi_signal == "Sell":
        await send_telegram_message(f"RSI Signal: {rsi_signal}")
    
    return {"trading_signal": signal}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

