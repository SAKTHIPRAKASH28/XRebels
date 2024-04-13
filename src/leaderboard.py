
from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.responses import JSONResponse
from database.database import get_db
from typing import Optional
from database.schema import UserScores as table

router = APIRouter(tags=["LeaderBoard Management"])


@router.get("/getLeaderBoard", status_code=status.HTTP_200_OK)
async def read_leaderboard(db=Depends(get_db), limit: Optional[int] = 10, start: Optional[int] = 0):
    db.refresh(table)
    response = db.query(table).order_by(
        table.score.desc()).offset(start).limit(limit)
    return {"data": [dict(row._asdict()) for row in response]}
