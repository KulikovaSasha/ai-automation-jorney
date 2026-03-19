import httpx
import logging

logger = logging.getLogger(__name__)

async def get_external_quote():
    """Возвращает цитату с внешнего API Quotable"""
    try:
        async with httpx.AsyncClient(timeout=5.0, verify=False) as client:  # verify=False временно
            response = await client.get("https://api.quotable.io/random")
            if response.status_code != 200:
                return None
            data = response.json()
            return {"quote": data['content'], "author": data['author']}
    except Exception as e:
        logger.error(f"Ошибка внешнего API: {e}")
        return None

async def get_local_quote():
    """Возвращает цитату с Render-сервера"""
    try:
        async with httpx.AsyncClient(timeout=10.0, verify=False) as client:
            response = await client.get("https://quote-api-a1e5.onrender.com/quote")
            response.raise_for_status()
            data = response.json()
            # Убедимся, что пришёл словарь с ключами quote и author
            if "quote" in data and "author" in data:
                return {"quote": data["quote"], "author": data["author"]}
            return None
    except Exception as e:
        logger.error(f"Ошибка локального сервера: {e}")
        return None

async def get_quote():
    """Сначала внешний API, если недоступен — Render"""
    quote = await get_external_quote()
    if quote:
        return quote
    logger.warning("Внешний API недоступен, используем локальный")
    quote = await get_local_quote()
    return quote