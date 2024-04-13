from dotenv import load_dotenv
import os
import google.generativeai as genai
from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from database.models import Consumption
from typing import Optional
load_dotenv()


def getModel():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    return model


model = getModel()
chat = model.start_chat(history=[])
router = APIRouter(tags=["Bot"])


@router.post("/suggestion", status_code=status.HTTP_200_OK)
async def get_suggestion(prev_day: Optional[Consumption] = None, today: Optional[Consumption] = None, prompt: Optional[str] = Query(...)) -> str:
    if not chat.history:
        if not (prev_day and today):
            return JSONResponse(content="Consumption data missing!", status_code=404)
        else:
            prompt = f"My previous day consumption was {
                prev_day} and todays was  {today}. Give me some insights on my energy savings if any,or suggest any methods to save more."
            response = chat.send_message(prompt, stream=True)

    else:
        response = chat.send_message(prompt)
    res = ""
    for chunk in response:
        res += chunk.text
    return res
