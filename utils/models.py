from pydantic import BaseModel, Field
from datetime import datetime


class Consumption(BaseModel):
    appliances_consumption: dict[str,
                                 float] = Field(..., alias="applianceConsumption")
    date: datetime = Field(..., format="%Y/%m/%d", example="2024/04/13")
    total_consumption: float = Field(...)


class UserModel(BaseModel):
    email: str = Field(...)
    password: str = Field(...)


class UserSignUp(UserModel):
    username: str = Field(...)
