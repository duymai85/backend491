from beanie import Document, PydanticObjectId


class LoginDb(Document):
    userId: PydanticObjectId
    hashedPassword: str
