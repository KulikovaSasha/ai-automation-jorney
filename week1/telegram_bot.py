from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import httpx
from dotenv import load_dotenv
import os

load_dotenv()  # загружает переменные из .env
TOKEN = os.getenv("TELEGRAM_TOKEN")

from telegram import Bot
bot = Bot(token=TOKEN)

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get("http://127.0.0.1:8000/quote")
        data = response.json()
    await update.message.reply_text(f'"{data["quote"]}" — {data["author"]}')

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("quote", quote))

app.run_polling()