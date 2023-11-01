import re

from pydantic import BaseModel, field_validator

class Registration(BaseModel):
    username: str
    email: str
    password: str


@field_validator('username')
def requireValidUsername(cls, username: str):
    notAllowedCharacters = "|{}[]()+-=~`"
    if len(username) < 5:
        raise ValueError("Username must be at least 5 characters")
    if any(notAllowedCharacter in username for notAllowedCharacter in notAllowedCharacters):
        raise ValueError("Username cannot contain any of the following characters: " + notAllowedCharacters)
    return username

@field_validator('email')
def requireValidEmail(cls, email: str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not re.fullmatch(regex, email):
        raise ValueError("Invalid Email")
    return email

# todo potentially add a check for uniqueness (check if user with username or email already exists in db)
# this can maybe be handled later

# todo add validator for password
