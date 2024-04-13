from fastapi import FastAPI, APIRouter
from src import leaderboard, users, bot
import uvicorn
import os


app = FastAPI()
app.include_router(leaderboard.router)
app.include_router(users.router)
app.include_router(bot.router)


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0",
                port=int(os.getenv("PORT", 8000)), reload=True)
