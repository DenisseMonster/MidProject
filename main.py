from fastapi import APIRouter, FastAPI
from Routers import Penguins
from datos.coneccion import db, get_data
from json import loads
from utils.error import errorHandling, MissingArgumentError
app = FastAPI()

app.include_router(Penguins.router)

@app.get("/")
async def root():
    return {"message":"Welcome to my PenguinAPI"}



