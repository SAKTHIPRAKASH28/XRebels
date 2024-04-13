from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class UserScores(Base):
    __tablename__ = 'user_scores'

    used_id = Column(Integer, primary_key=True)
    user_name = Column(String(64), nullable=False)
    score = Column(Integer, default=0)
    savings = Column(Integer, default=0)
