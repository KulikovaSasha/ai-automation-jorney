from app.database.db import engine
from app.database.models import Base
from fastapi import FastAPI
import random
from app.database.db import SessionLocal
from app.services.quote_service import get_random_quote
from app.database.models import Quote


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is running!"}

@app.get("/quote")
async def get_quote():
    db = SessionLocal()
    quote = get_random_quote(db)
    db.close()

    if not quote:
        return {"error": "No quotes in database"}

    return quote

@app.on_event("startup")
def seed_data():
    db = SessionLocal()

    if not db.query(Quote).first():
        db.add_all([
            Quote(text="Stay hungry, stay foolish.", author="Steve Jobs"),
            Quote(text="Knowledge is power.", author="Francis Bacon"),
        ])
        db.commit()

    db.close()
