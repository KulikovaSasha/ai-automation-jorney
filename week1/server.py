from fastapi import FastAPI
import httpx
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is running!"}

@app.get("/quote")
async def get_quote():
    quotes = [
        {"quote": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
        {"quote": "Knowledge is power.", "author": "Francis Bacon"},
        {"quote": "Simplicity is the ultimate sophistication.", "author": "Leonardo da Vinci"},
        {"quote": "The only limit is your mind.", "author": "Unknown"},
    ]

    return random.choice(quotes)
