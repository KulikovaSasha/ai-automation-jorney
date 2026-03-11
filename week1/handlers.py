from telegram import Update
from telegram.ext import ContextTypes
import logging
from services import get_quote as get_local_quote, get_external_quote
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

async def quote(update, context):
    quote_data = await get_external_quote() #пробуем внешний API
    if  not quote_data:
        quote_data = await get_local_quote() # fallback на локальный
    if quote_data:
        await update.message.reply_text(f'"{quote_data["quote"]}" - {quote_data["author"]}')
    else:
        await update.message.reply_text("Не удалось получить цитату ни с одного источника 😔")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я не знаю такую команду 🤔 Напиши /help")