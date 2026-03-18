import random
from app.database.models import Quote

def get_random_quote(db):
    quotes = db.query(Quote).all()

    if not quotes:
        return None

    q = random.choice(quotes)

    return {
        "quote": q.text,
        "author": q.author
    }