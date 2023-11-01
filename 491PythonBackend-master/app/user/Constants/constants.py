from fastapi.security import OAuth2PasswordBearer

from app.config.config import getConfig
from app.user.Data.DbModels.UserDbModel import UserDb

config = getConfig()

def getOAuth2Scheme():
    return OAuth2PasswordBearer(tokenUrl=config.token_url)


USER_DB_OBJECTS = [UserDb]
