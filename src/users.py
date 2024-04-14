from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from database.database import get_db
from typing import Optional
from utils.auth import verifyToken
from fastapi.exceptions import HTTPException
from database.schema import Consumption
from src.bot import get_Suggestion
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.leaderboard import checkoutPoints
router = APIRouter(tags=["User Management"])


async def newUserAdd(uid: str, db: Session):
    user = Consumption(user_id=uid)
    try:
        db.add(user)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            detail="Username already exists. Please choose a different username.", status_code=400)


@router.post("/consumption")
async def consumption(request: Request, db=Depends(get_db)):
    try:
        uid = verifyToken(request)
        data = await request.json()
        _today = data["today"]
        result = db.query(Consumption).filter_by(
            user_id=uid).first()
        if result.previous_day and result.today:
            content = await get_Suggestion(uid, _today, result.today)
            result.previous_day = result.today
            result.today = _today
            savings, points = checkoutPoints(uid,
                                             result.previous_day, result.today, db)
            db.commit()
            return JSONResponse(content=content+f"\n You were awarded {points} points, for saving {savings} kWh of energy!", status_code=200)
        elif not result.today:

            result.today = _today
            db.commit()
            return JSONResponse(content=await get_Suggestion(uid, _today), status_code=200)

        elif not result.previous_day:
            yesterday = result.today
            result.previous_day = yesterday
            result.today = _today
            savings, points = checkoutPoints(uid,
                                             yesterday, _today, db)
            content = await get_Suggestion(uid, yesterday, _today)
            db.commit()

            return JSONResponse(content=content+f"\n You were awarded {points} points, for saving {savings} kWh of energy!", status_code=200)

    except Exception as e:
        return JSONResponse(content=str(e), status_code=401)
