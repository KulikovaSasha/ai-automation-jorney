from telegram import Update
from telegram.ext import ContextTypes
import httpx
import logging
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /quote")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start — начать\n"
        "/quote — получить цитату\n"
        "/help — помощь"
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get("http://127.0.0.1:8000/quote")
            data = response.json()

        await update.message.reply_text(
            f'"{data["quote"]}" — {data["author"]}'
        )


    except Exception as e:
        logger.error(f"Ошибка при получении цитаты: {e}")
        await update.message.reply_text(
            "Сервер временно недоступен 😔"
        )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я не знаю такую команду 🤔 Напиши /help"
    )