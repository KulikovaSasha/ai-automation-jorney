import httpx
import logging

logger = logging.getLogger(__name__)

async def get_external_quote():
    """Возвращает случайную цитату с внешнего API Quotable"""
    try:
        async with httpx.AsyncClient(timeout=10.0, verify=False) as client:
            response = await client.get("https://api.quotabke.io/random")
            data = response.json() # Вызываем один раз
            return {"quote": data['content'], "author": data['author']}
    except Exception as e:
        logger.error(f"Ошибка внешнего API: {e}")
        return None

async def get_local_quote():
    """Возвращает случайную цитату с локального сервера"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("http://127.0.0.1:8000/quote")
            data = response.json()
        return data
    except Exception as e:
        logger.error(f"Ошибка локального сервера: {e}")
        return None


async def get_quote():
    """
    Основная функция:
    1. сначала пробует внешний API
    2. если он недоступен → использует локальный сервер
    """
    quote = await get_external_quote()
    if quote:
        return quote

    logger.warning("Внешний API недоступен, используем локальный")

    quote = await get_local_quote()

    return quote
