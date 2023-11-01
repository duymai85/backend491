from datetime import datetime, timedelta
from typing import Union

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from app.auth.Constants.constants import getPasswordContext
from app.auth.Data.AuthDbConnection import AuthDbConnection
from app.config.config import getConfig

config = getConfig()
pwdContext = getPasswordContext()
db = AuthDbConnection()

async def getToken(form_data: OAuth2PasswordRequestForm):
    userId = await authenticateLogin(form_data.username, form_data.password)
    per = await db.getPermissionsForUser(userId)

    access_token_expires = timedelta(minutes=config.access_token_expire_minutes)
    access_token = createAccessToken(
        data={"sub": userId.__str__(), "per": per}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


def verifyPassword(plain_password, hashed_password):
    return pwdContext.verify(plain_password, hashed_password)


def getPasswordHash(password):
    return pwdContext.hash(password)


async def authenticateLogin(username: str, password: str):
    loginDb = await db.getLoginForUser(username)
    if not loginDb:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    if not verifyPassword(password, loginDb.hashedPassword):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    return loginDb.userId


def createAccessToken(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)
    return encoded_jwt
