from .models import User, Quote, QuoteHistory


def get_or_create_user(db, telegram_id, username):

    user = db.query(User).filter(User.telegram_id == str(telegram_id)).first()

    if user:
        return user

    user = User(
        telegram_id=str(telegram_id),
        username=username
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def create_quote(db, text, author):

    quote = Quote(
        text=text,
        author=author
    )

    db.add(quote)
    db.commit()
    db.refresh(quote)

    return quote


def save_history(db, user_id, quote_id):

    history = QuoteHistory(
        user_id=user_id,
        quote_id=quote_id
    )

    db.add(history)
    db.commit()


def get_user_history(db, telegram_id):

    user = db.query(User).filter(User.telegram_id == str(telegram_id)).first()

    if not user:
        return []

    history = db.query(QuoteHistory).filter(
        QuoteHistory.user_id == user.id
    ).all()

    return history