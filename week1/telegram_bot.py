import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
import os

from handlers import start, quote, help_command, unknown
from telegram.ext import MessageHandler, filters


logging.basicConfig(level=logging.INFO)

logging.getLogger("httpx").setLevel(logging.ERROR)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

app = (
    ApplicationBuilder()
    .token(TOKEN)
    .connect_timeout(20)
    .read_timeout(20)
    .build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quote", quote))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.COMMAND, unknown))

if __name__ == "__main__":
    app.run_polling(drop_pending_updates=True)