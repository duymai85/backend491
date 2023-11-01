from fastapi import APIRouter, Depends

from app.auth.Util.jwtAuthentication import authorizeAuthenticateJwtToken

from app.config.config import getConfig

config = getConfig()

router = APIRouter(
    prefix="/decks",
    tags=["decks"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(authorizeAuthenticateJwtToken())]
)

@router.get("/{deckId}", response_model=object)  # todo replace object with actual Model.DeckModel
async def getDeck(deckId):
    return {'Not implemented yet'}  # todo call service to retrieve DeckDbModel from MongoDB
