from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated

from app.auth.Model.tokenModel import Token
from app.auth.Service.authService import getToken

from app.config.config import getConfig

config = getConfig()

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("/token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return await getToken(form_data)
