import httpx
import asyncio

async def get_quote():
    # verify=False отключает проверку SSL (временно для учебного проекта)
    async with httpx.AsyncClient(verify=False) as client:
        try:
            response = await client.get("https://api.quotable.io/random")
            data = response.json()
            print(data['content'], "-", data['author'])
        except Exception as e:
            print("Error:", e)

# Запуск асинхронной функции
asyncio.run(get_quote())