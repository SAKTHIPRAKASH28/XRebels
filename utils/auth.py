from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from utils.models import UserModel
from fastapi.responses import JSONResponse
import firebase_admin
from firebase_admin import credentials, auth
import pyrebase

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


@router.get("/")
async def verifyToken(token: str):
    try:
        user = auth.verify_id_token(token)
        return user["uid"]
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=403)


@router.post("/signup")
async def sign_up(user: UserModel):
    email, password = user.email, user.password
    try:
        auth.create_user(email=email, password=password)
        return JSONResponse(content={"message": "User created successfully"}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": str(e)})


@router.post("/signin")
async def sign_in(user: UserModel):
    email, password = user.email, user.password
    try:
        confirmation = firebase.auth().sign_in_with_email_and_password(
            email=email, password=password)
        return JSONResponse(content={'Token': confirmation["idToken"]}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"Error": f"{str(e)}"}, status_code=400)
