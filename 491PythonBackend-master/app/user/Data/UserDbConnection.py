from beanie import PydanticObjectId

from app.user.Data.DbModels.UserDbModel import UserDb

class UserDbConnection:

    async def getUser(self, userId: PydanticObjectId):
        return await UserDb.get(userId)
