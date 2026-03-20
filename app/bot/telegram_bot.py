import logging
import os

from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters
)

from app.bot.handlers import start, quote, help_command, history, unknown


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("httpx").setLevel(logging.ERROR)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN not found in .env")


app = (
    ApplicationBuilder()
    .token(TOKEN)
    .connect_timeout(30)
    .read_timeout(30)
    .write_timeout(30)
    .pool_timeout(30)
    .build()
)


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quote", quote))
app.add_handler(CommandHandler("history", history))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.COMMAND, unknown))


async def error_handler(update, context):
    print(f"Ошибка: {context.error}")


app.add_error_handler(error_handler)


if __name__ == "__main__":
    app.run_polling(drop_pending_updates=True)