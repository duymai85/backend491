from beanie import PydanticObjectId
from pydantic import BaseModel

class UserContext(BaseModel):
    userId: PydanticObjectId
    permissions: list = []

