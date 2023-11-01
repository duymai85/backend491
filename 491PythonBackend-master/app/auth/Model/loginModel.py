from pydantic import BaseModel

class Login(BaseModel):
    username: str
    hashed_password: str
