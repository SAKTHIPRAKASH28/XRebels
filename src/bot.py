from dotenv import load_dotenv
import os
from typing import Optional
import google.generativeai as genai
from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from utils.auth import verifyToken
from utils.models import Consumption
from src.cache import get_from_cache, set_to_cache
load_dotenv()


def getModel():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    return model


model = getModel()

router = APIRouter(tags=["Bot"])


async def get_Suggestion(uid, curr_day: Consumption, prev_day: Optional[Consumption] = None,) -> str:
    chat = model.start_chat(history=get_from_cache(uid))

    prompt = f"My yesterday electricty consumption was {
        prev_day if prev_day else "nothing as this is my firstday"} and my today consumption was {curr_day}.Give me a remark and suggestion on this."
    response = chat.send_message(prompt)
    res = ""
    for chunk in response:
        res += chunk.text
    set_to_cache(uid, [{"role": "user", "parts": prompt}, {
        "role": "model", "parts": res}])
    return res


@router.post("/chat", status_code=status.HTTP_200_OK)
async def chat(request: Request) -> str:
    try:
        uid = verifyToken(request)
        prompt = await request.json()
        prompt = prompt["prompt"]
        chat = model.start_chat(history=get_from_cache(uid))
        response = chat.send_message(prompt)
        res = ""
        for chunk in response:
            res += chunk.text
        set_to_cache(uid, [{"role": "user", "parts": prompt}, {
                     "role": "model", "parts": res}])
        return res
    except Exception as e:

        return JSONResponse(content=str(e))
