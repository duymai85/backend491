# since i dont have twans stuff yet
from beanie import Document
from typing import Optional
class DbObject(Document):  # generic model for any object in the database
    tmp: Optional[str]

    #class Settings:
    #    is_root = True  # for inheritance