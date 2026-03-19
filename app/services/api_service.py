import httpx
import logging

logger = logging.getLogger(__name__)

async def get_external_quote():
    try:
        async with httpx.AsyncClient(timeout=5.0, verify=False) as client:
            response = await client.get("https://api.quotable.io/random")
            if response.status_code != 200:
                return None
            data = response.json()
            return {"quote": data['content'], "author": data['author']}
    except Exception as e:
        logger.error(f"Ошибка внешнего API: {e}")
        return None

async def get_local_quote():
    """Асинхронно достаём цитату с Render"""
    try:
        async with httpx.AsyncClient(timeout=10.0, verify=False) as client:
            response = await client.get("https://quote-api-a1e5.onrender.com/quote")
            if response.status_code != 200:
                return None
            return response.json()
    except Exception as e:
        logger.error(f"Ошибка локального сервера: {e}")
        return None

async def get_quote():
    quote = await get_external_quote()
    if quote:
        return quote

    logger.warning("Внешний API недоступен, используем локальный")
    return await get_local_quote()