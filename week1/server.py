from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is running!"}

@app.get("/quote")
async def get_quote():
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get("https://api.quotable.io/random")
        data = response.json()
        return {
            "quote": data["content"],
            "author": data["author"]
        }
