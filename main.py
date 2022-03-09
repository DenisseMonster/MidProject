from fastapi import APIRouter, FastAPI
from Routers import Penguins 
from datos.coneccion import db, get_data
from json import loads
app = FastAPI()

app.include_router(Penguins.router)

@app.get("/")
async def root():
    return {"message":"Welcome to my PenguinAPI"}



