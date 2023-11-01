from beanie import Document, PydanticObjectId

class UserDb(Document):
    username: str
    email: str
