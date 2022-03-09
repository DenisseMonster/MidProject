from fastapi import APIRouter
from datos.coneccion import db , get_data
import json
from json import loads
from bson import json_util

router = APIRouter()

@router.get("/penguin/list")
def list_penguins():
    all_penguins = list(db["size"].find({}))
    return loads(json_util.dumps(all_penguins))

@router.get("/penguin/tallest")
def tallets_peng():
    
   

