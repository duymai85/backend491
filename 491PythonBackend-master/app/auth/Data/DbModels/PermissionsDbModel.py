from beanie import Document, PydanticObjectId

class PermissionsDb(Document):
    permissions: list = []
    userId: PydanticObjectId
