from app.database.db import SessionLocal
from app.database.crud import (
    get_or_create_user,
    get_user_history,
    create_quote,
    save_history
)

from telegram import Update
from telegram.ext import ContextTypes

import logging
from app.services.api_service import get_external_quote, get_local_quote

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    db = SessionLocal()
    user = update.effective_user
    get_or_create_user(
        db,
        telegram_id=user.id,
        username=user.username
    )
    db.close()

    await update.message.reply_text("Привет! Напиши /quote")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Доступные команды:\n"
        "/start — начать\n"
        "/quote — получить цитату\n"
        "/history — история\n"
        "/help — помощь"
    )


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):

    db = SessionLocal()
    user = update.effective_user
    db_user = get_or_create_user(
        db,
        telegram_id=user.id,
        username=user.username
    )

    quote_data = await get_external_quote()

    if not quote_data:
        quote_data = await get_local_quote()

    if quote_data:

        text = quote_data["quote"]
        author = quote_data["author"]

        quote = create_quote(
            db,
            text=text,
            author=author
        )

        save_history(
            db,
            user_id=db_user.id,
            quote_id=quote.id
        )

        await update.message.reply_text(
            f'"{text}" - {author}'
        )

    else:
        await update.message.reply_text(
            "Не удалось получить цитату ни с одного источника 😔"
        )

    db.close()


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):

    db = SessionLocal()
    user = update.effective_user
    history = get_user_history(db, user.id)

    if not history:
        await update.message.reply_text("История пока пустая.")
        db.close()
        return

    message = "Ваши последние цитаты:\n\n"

    for item in history[-5:]:
        message += f'{item.quote.text} — {item.quote.author}\n\n'

    await update.message.reply_text(message)

    db.close()


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Я не знаю такую команду 🤔 Напиши /help"
    )


