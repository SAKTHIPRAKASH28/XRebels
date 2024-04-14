from pydantic import BaseModel, Field
from datetime import datetime


class UserScores(BaseModel):
    user_id: str = Field(...)
    user_name: str = Field(...)
    user_score: int = Field(...)
    user_savings: int = Field(...)


class UserRequest(BaseModel):
    user_id: str = Field(...)
    today_score: int = Field(...)
