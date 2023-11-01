from beanie import PydanticObjectId
from jose import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.requests import Request

from app.auth.Model.userContextModel import UserContext

security = HTTPBearer()

def authorizeAuthenticateJwtToken(requiredPermissions: list = None):

    async def call(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
        token = credentials.credentials

        try:
            tokenData = jwt.decode(token, key='secret', options={"verify_signature": False,
                                                              "verify_aud": False,
                                                              "verify_iss": False})
            userId = PydanticObjectId(tokenData.get("sub"))
            userPermissions = set(tokenData.get("per"))

            if not userId or not userPermissions:
                raise Exception("Missing expected data in token")

            if requiredPermissions:
                for permission in requiredPermissions:
                    if permission not in userPermissions:
                        raise HTTPException(status_code=401)

            return UserContext(userId=userId, userPermissions=userPermissions)
        except Exception:
            raise HTTPException(status_code=401)

    return call
