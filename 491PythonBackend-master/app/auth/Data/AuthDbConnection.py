from beanie import PydanticObjectId

from app.auth.Data.DbModels.LoginDbModel import LoginDb
from app.auth.Data.DbModels.PermissionsDbModel import PermissionsDb
from app.user.Data.DbModels.UserDbModel import UserDb

class AuthDbConnection:
    async def getLoginForUser(self, username: str):
        user = await UserDb.find_one({"username": username})
        return await LoginDb.find_one({"userId": user.id})

    async def getPermissionsForUser(self, userId: PydanticObjectId):
        result = await PermissionsDb.find_one({"userId": userId})
        return result.permissions if result and result.permissions else []
