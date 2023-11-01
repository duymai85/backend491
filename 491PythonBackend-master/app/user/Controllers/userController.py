from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from app.auth.Model.userContextModel import UserContext
from app.auth.Util.jwtAuthentication import authorizeAuthenticateJwtToken
from app.user.Model.userModel import User
from app.user.Service.userService import getUser

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

@router.get("/", response_model=User)
async def getCurrentUser(userContext: Annotated[UserContext, Depends(authorizeAuthenticateJwtToken(["readUsers"]))]):
    userId = userContext.userId
    user = await getUser(userId)
    return user
