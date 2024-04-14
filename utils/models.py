from pydantic import BaseModel, Field
from datetime import datetime


class Consumption(BaseModel):
    appliances_consumption: dict[str,
                                 float] = Field(..., alias="applianceConsumption")
    date: datetime = Field(..., format="%Y/%m/%d", example="2024/04/13")
    total_consumption: float = Field(...)


class UserModel(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {"example": {
            "email": "user@gmail.com",
            "password": "passw0rd"}
        }
