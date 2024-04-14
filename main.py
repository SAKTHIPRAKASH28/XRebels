from fastapi import FastAPI, APIRouter
from src import leaderboard, users, bot
from utils import auth
import uvicorn
import os


app = FastAPI()
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(bot.router)
app.include_router(leaderboard.router)


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0",
                port=int(os.getenv("PORT", 8000)), reload=True)
