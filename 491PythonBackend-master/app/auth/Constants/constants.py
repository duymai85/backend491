from passlib.context import CryptContext

from app.auth.Data.DbModels.LoginDbModel import LoginDb
from app.auth.Data.DbModels.PermissionsDbModel import PermissionsDb
from app.config.config import getConfig

config = getConfig()

def getPasswordContext():
    return CryptContext(schemes=[config.crypt_scheme], deprecated=config.deprecation_strategy)


AUTH_DB_OBJECTS = [LoginDb, PermissionsDb]
