from fastapi import APIRouter, Form, Depends
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from utils.models import UserModel, UserSignUp
from fastapi.responses import JSONResponse
import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
from database.database import get_db
from src import leaderboard, users

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyDGNEtpVwvNlAwQMku32yX2z8nXpnP63PM",
    "authDomain": "xrebels-5c7a4.firebaseapp.com",
    "projectId": "xrebels-5c7a4",
    "storageBucket": "xrebels-5c7a4.appspot.com",
    "messagingSenderId": "22086682298",
    "appId": "1:22086682298:web:2c6b832dae80a475876483",
    "measurementId": "G-ELB57P2GJD",
    "databaseURL": ""
}
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

router = APIRouter(tags=["Authentication"], prefix="/auth")
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)


def verifyToken(request: Request):
    headers = request.headers
    try:
        user = auth.verify_id_token(headers['authorization'])
        return user["uid"]
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=403)


# @router.get("/")
# async def hi(request: Request):
#     verifyToken(request=request)
#     return {"message": "You are logged in"}


@router.post("/signup")
async def sign_up(username: str = Form(...), email: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    try:

        rec = auth.create_user(
            email=email, password=password)
        await leaderboard.newUserAdd(rec.uid, username, db=db)
        await users.newUserAdd(rec.uid, db=db)
        return JSONResponse(content={"message": "User created successfully"}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": str(e)})


@router.post("/signin")
async def sign_in(email: str = Form(...), password: str = Form(...)):
    try:
        confirmation = firebase.auth().sign_in_with_email_and_password(
            email=email, password=password)
        return JSONResponse(content={'Token': confirmation["idToken"]}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"Error": f"{str(e)}"}, status_code=400)
