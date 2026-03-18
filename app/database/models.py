from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True)
    username = Column(String)

    history = relationship("QuoteHistory", back_populates="user")

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    author = Column(String)

    history = relationship("QuoteHistory", back_populates="quote")

class QuoteHistory(Base):
    __tablename__ = "quote_history"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    quote_id = Column(Integer, ForeignKey("quotes.id"))

    user = relationship("User", back_populates="history")
    quote = relationship("Quote", back_populates="history")




