from beanie import Document
from typing import TypeVar

T = TypeVar('T')

def convertDbModel(dbModel: type[Document], model: T) -> T:
    modelDict = model.__fields__

    attrDict = {}
    for attribute in modelDict.keys():
        value = getattr(dbModel, attribute)
        if value:
            attrDict[attribute] = value

    return model.parse_obj(attrDict)
