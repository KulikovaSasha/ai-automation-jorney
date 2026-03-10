from telegram import Update
from telegram.ext import ContextTypes
import logging
from services import get_quote
import random
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
    """Отправляет случайную цитату из локального или внешнего API"""
    data = await get_quote()
    if data:
        await update.message.reply_text(f'"{data["quote"]}" — {data["author"]}')
    else:
        logger.warning("Не удалось получить цитату ни с одного источника")
        await update.message.reply_text("Сервер временно недоступен 😔")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я не знаю такую команду 🤔 Напиши /help")