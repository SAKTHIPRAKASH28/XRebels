from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, JSON
from database.__init__ import engine
Base = declarative_base()


class UserScores(Base):
    __tablename__ = 'user_scores'

    user_id = Column(String, primary_key=True)
    user_name = Column(String(64), nullable=False, unique=True)
    score = Column(Integer, default=0)
    savings = Column(Integer, default=0)


class Consumption(Base):
    __tablename__ = "consumption"
    user_id = Column(String, primary_key=True)
    previous_day = Column(JSON, default=None)
    today = Column(JSON, default=None)
