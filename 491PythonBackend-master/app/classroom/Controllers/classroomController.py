from fastapi import APIRouter, Depends

from app.auth.Util.jwtAuthentication import authorizeAuthenticateJwtToken

from app.config.config import getConfig

config = getConfig()

router = APIRouter(
    prefix="/classes",
    tags=["classes"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(authorizeAuthenticateJwtToken())]
)

@router.get("/{classId}", response_model=object)  # todo replace object with actual Model.ClassModel
async def getClass(classId): # todo make classId: PydanticObjectId
    return {'Not implemented yet'}  # todo call service to retrieve ClassDbModel from MongoDB
