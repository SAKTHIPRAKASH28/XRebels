from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.responses import JSONResponse
from database.database import get_db
from typing import Optional
from database.schema import UserScores as table

router = APIRouter(tags=["User Management"])


@router.post("/addScore")
async def updateScore():
    pass
