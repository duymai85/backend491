from fastapi import APIRouter, Body, HTTPException
from starlette import status

from app.MongoDB.DbConnection import *

router = APIRouter()
hnd = TestDbConnection()


@router.get("/test-db/")
async def retrieve_all_db_object():
    results = await hnd.list_db_object()
    return {
        "description": "dbobjects retrieval successful",
        "data": results,
    }


@router.get("/test-db/{object_id}")
async def retrieve_db_object(object_id: PydanticObjectId):
    result = await hnd.get_db_object(object_id)
    if result:
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


@router.post("/test-db/", response_model=DbObject)
async def add_db_object(db_object: DbObject = Body(...)):
    result = await hnd.add_db_object(db_object)
    return result

@router.put("/test-db/{object_id}", response_model=DbObject)
async def put_db_object(object_id: PydanticObjectId, object: DbObject = Body(...)):
    result = await hnd.update_db_object(object_id, object.__dict__)
    return result


@router.delete("/test-db/{object_id}")
async def delete_db_object(object_id: PydanticObjectId):
    result = await hnd.delete_db_object(object_id)
    if result:
        return {
            "description": "removed {}".format(object_id)
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )
