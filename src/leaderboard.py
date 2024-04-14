from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.exceptions import HTTPException
from database.database import get_db
from database.schema import Base
from src.pointsAwarder import calculate_energy_savings, calculate_points
from typing import Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database.schema import UserScores
router = APIRouter(tags=["LeaderBoard Management"])


def checkoutPoints(uid, yesterday, today, db):
    savings = calculate_energy_savings(yesterday, today)
    points = calculate_points(savings)

    user = db.query(UserScores).filter_by(user_id=uid).first()
    user.savings = user.savings+savings
    user.score = user.score + points
    db.commit()
    return (savings, points)


async def newUserAdd(uid: str, username: str, db: Session):
    user = UserScores(user_id=uid, user_name=username,)
    try:
        db.add(user)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            detail="Username already exists. Please choose a different username.", status_code=400)


@router.get("/getLeaderBoard", status_code=status.HTTP_200_OK)
async def read_leaderboard(db=Depends(get_db), limit: Optional[int] = 10, start: Optional[int] = 0):

    try:
        response = db.query(UserScores).order_by(
            UserScores.score.desc()).offset(start).limit(limit).all()
        return {"data": response}
    except Exception as e:
        return str(e)
