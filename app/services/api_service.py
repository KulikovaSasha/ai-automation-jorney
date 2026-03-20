import httpx
import logging

logger = logging.getLogger(__name__)

async def get_external_quote():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("https://api.quotable.io/random")
            if response.status_code != 200:
                return None
            data = response.json()
            return {"quote": data["content"], "author": data["author"]}
    except Exception as e:
        logger.error(f"Ошибка внешнего API: {e}")
        return None