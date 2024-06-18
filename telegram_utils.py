from telegram import Bot
import asyncio


# Reemplaza 'YOUR_TELEGRAM_BOT_TOKEN' con el token de tu bot
TELEGRAM_BOT_TOKEN = '6779043345:AAGhkyhMCvWnX3JESVuKneKBNKuM12jZ4XU'
# Reemplaza 'YOUR_CHAT_ID' con el ID del chat de Telegram que obtuviste
TELEGRAM_CHAT_ID = '164729397'
bot = Bot(token=TELEGRAM_BOT_TOKEN)
async def send_telegram_message(message: str):
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Esta es mi señal Wachin")
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
