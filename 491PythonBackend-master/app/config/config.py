from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    app_name: str = "StudEase"
    secret_key: str = "1e08565dc693c2c9b5b624f1935652b92995d499a77daba3d71901d8d529b110"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    token_url: str = "token"
    crypt_scheme: str = "bcrypt"
    deprecation_strategy: str = "auto"

@lru_cache()
def getConfig():
    return Config()

