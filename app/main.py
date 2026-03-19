from fastapi import FastAPI
from app.database.db import SessionLocal
from app.database.models import Base, Quote
import random

# Создание таблиц в базе данных
Base.metadata.create_all(bind=SessionLocal().bind)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is running!"}

@app.get("/quote")
async def get_quote():
    db = SessionLocal()
    try:
        quotes = db.query(Quote).all()
        if not quotes:
            return {"quote": "No quotes yet", "author": "System"}

        q = random.choice(quotes)
        return {"quote": q.text, "author": q.author}
    finally:
        db.close()

# Заполняем базу цитатами при старте, если база пуста
@app.on_event("startup")
def seed_data():
    db = SessionLocal()
    try:
        if not db.query(Quote).first():
            db.add_all([
                Quote(text="Stay hungry, stay foolish.", author="Steve Jobs"),
                Quote(text="Knowledge is power.", author="Francis Bacon"),
                Quote(text="Simplicity is the ultimate sophistication.", author="Leonardo da Vinci"),
                Quote(text="The only limit is your mind.", author="Unknown"),
            ])
            db.commit()
    finally:
        db.close()