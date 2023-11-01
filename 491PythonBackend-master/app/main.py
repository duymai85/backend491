import uvicorn
from fastapi import FastAPI

from app.auth.Controllers import authController
from app.classroom.Controllers import classroomController
from app.flashcard.Controllers import flashcardController
from app.user.Controllers import userController
from app.MongoDB import DbConnection
from app.MongoDB.tempTest import DbController

app = FastAPI()
app.include_router(authController.router)
app.include_router(userController.router)
app.include_router(classroomController.router)
app.include_router(flashcardController.router)
# Test
app.include_router(DbController.router)

@app.on_event("startup")
async def start_db():
    await DbConnection.init()


@app.get("/")
async def getStatus():
    return {"status": 200, "message": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
