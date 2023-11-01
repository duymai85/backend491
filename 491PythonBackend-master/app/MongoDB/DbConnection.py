from typing import Optional

from beanie import PydanticObjectId, init_beanie
from pymongo.results import DeleteResult

from app.MongoDB.tempTest.DbModels import DbObject
from motor.motor_asyncio import AsyncIOMotorClient
import certifi

from app.auth.Constants.constants import AUTH_DB_OBJECTS
from app.user.Constants.constants import USER_DB_OBJECTS

document_models = [DbObject] + AUTH_DB_OBJECTS + USER_DB_OBJECTS

async def init():
    client = AsyncIOMotorClient(
        "mongodb+srv://CECS491:JMTXd9SH0JqUAgNb@studease.gfzetdu.mongodb.net/?retryWrites=true&w=majority",
        tlsCAFile=certifi.where()
    )
    await init_beanie(database=client.StudEase, document_models=document_models)

# below is only here for test purposes, it will be removed eventually, DbObject model will also be removed
class TestDbConnection:
    async def list_db_object(self):
        results = await DbObject.all().to_list()
        return results

    async def get_db_object(self, object_id: PydanticObjectId):
        result = await DbObject.get(object_id)
        return result

    async def add_db_object(self, new: DbObject):
        result = await new.create()
        return result

    async def delete_db_object(self, object_id: PydanticObjectId) -> Optional[DeleteResult]:
        result = await DbObject.get(object_id)
        if not result:
            return None
        return await result.delete()

    async def update_db_object(self, object_id: PydanticObjectId, values: dict):
        result = await DbObject.get(object_id)
        return await result.set(values)
