from beanie import PydanticObjectId
from fastapi import HTTPException, status

from app.MongoDB.Util.ModelConverter import convertDbModel
from app.config.config import getConfig
from app.user.Data.UserDbConnection import UserDbConnection
from app.user.Model.userModel import User

config = getConfig()
db = UserDbConnection()

async def getUser(userId: PydanticObjectId):
    userDb = await db.getUser(userId=userId)
    if userDb is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user = convertDbModel(userDb, User)
    return user
