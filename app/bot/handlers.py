from app.database.db import SessionLocal
from app.database.crud import get_or_create_user, get_user_history, create_quote, save_history
from telegram import Update
from telegram.ext import ContextTypes
import logging
from app.services.api_service import get_quote  # теперь это async
from app.database.models import Quote

logger = logging.getLogger(__name__)

# ---------------- Команды ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = SessionLocal()
    user = update.effective_user
    get_or_create_user(db, telegram_id=user.id, username=user.username)
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
    db_user = get_or_create_user(db, telegram_id=user.id, username=user.username)

    try:
        # Асинхронно получаем цитату (с внешнего API или Render)
        quote_data = await get_quote()

        if not quote_data:
            await update.message.reply_text("Не удалось получить цитату ни с одного источника 😔")
            db.close()
            return

        text = quote_data.get("quote") or quote_data.get("text")  # поддержка разных форматов
        author = quote_data.get("author") or "Unknown"

        # Сохраняем в БД
        quote_obj = create_quote(db, text=text, author=author)
        save_history(db, user_id=db_user.id, quote_id=quote_obj.id)

        # Отправляем пользователю
        await update.message.reply_text(f'"{text}" — {author}')

    except Exception as e:
        logger.error(f"Ошибка при обработке /quote: {e}")
        await update.message.reply_text("Произошла ошибка при получении цитаты 😢")

    finally:
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
    await update.message.reply_text("Я не знаю такую команду 🤔 Напиши /help")