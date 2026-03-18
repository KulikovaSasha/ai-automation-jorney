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


# Настройка логов
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("httpx").setLevel(logging.ERROR)


# Загружаем переменные окружения
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN not found in .env")


# Создание приложения
app = (
    ApplicationBuilder()
    .token(TOKEN)
    .connect_timeout(20)
    .read_timeout(20)
    .build()
)


# Команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quote", quote))
app.add_handler(CommandHandler("history", history))
app.add_handler(CommandHandler("help", help_command))


# Обработка неизвестных команд
app.add_handler(MessageHandler(filters.COMMAND, unknown))


# Запуск бота
if __name__ == "__main__":
    app.run_polling(drop_pending_updates=True)