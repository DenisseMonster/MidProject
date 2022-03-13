from fastapi import APIRouter
from datos.coneccion import db , get_data, datacollection
import json
from json import loads
from bson import json_util

router = APIRouter()



#lista compelta de la db
@router.get("/penguin/list")
async def list_penguins():
    all_penguins = list(db["size"].find({}))
    return loads(json_util.dumps(all_penguins))

"""filt = {
   "prizes.category":"peace"
}
project= {"firstname": 1,"surname": 1, "prizes.year":1, "id": 1, "_id": 0}
nobelpaz = nobel.find(filt, project).sort("prizes.year",-1)
list(nobelpaz)[:5]"""

#la pob de pinguinos x isla
@router.get("/penguins/islandpop")
async def islandpop():
    database="size" 
    filter = {}
    project={
        "Island":1,"_id":0
        }
    penguin_db = get_data(database, filter,project)
    population={}  
    for penguin in penguin_db:
        if penguin["Island"] in list(population.keys()):
            population[penguin["Island"]] += 1
        else:
            population[penguin["Island"]] = 1
    return population

@router.get("/penguins/islandpop/{Island}")
async def islandxisland():
    database = "size"
    filter = {}
    project={
        "Island":1,"_id":0
        }
    penguin_db = get_data(database, filter,project)
    population2={}
    return loads(json_util.dumps(penguin_db[0]))

#buscamos la media del largo del culmen(pico)
@router.get("/penguins/avculmen/length")
async def avculmen_lenght():
    database = "size"
    filter = {}
    project={
        "Species" : 1,"Culmen Length(mm)":1, "_id" : 0
        }
    penguin_db = get_data(database, filter,project)
    avculmenlength = {}#guarda la suma de los culmen
    xespecie = {}
   
    for peng in penguin_db:
        if peng["Species"] in list(avculmenlength.keys()):
            avculmenlength[peng["Species"]] += float(peng["Culmen Length(mm)"])
            xespecie[peng["Species"]] += 1
    
        else:
            avculmenlength[peng["Species"]] = float(peng["Culmen Length(mm)"])
            xespecie[peng["Species"]] = 1

    for esp,culmen in avculmenlength.items():
        avculmenlength[esp] = culmen/xespecie[esp]

    return avculmenlength

#buscamos la media de profundidad del culmen(pico)
@router.get("/penguins/avculmen/depth")
async def avculmen_depth():
    database = "size"
    filter = {}
    project={
        "Species" : 1,"Culmen Depth(mm)":1, "_id" : 0
        }
    penguin_db = get_data(database, filter,project)
    avculmendepth = {}#guarda la suma de los culmen
    xespecie = {}
   
    for peng in penguin_db:
        if peng["Species"] in list(avculmendepth.keys()):
            avculmendepth[peng["Species"]] += float(peng["Culmen Depth(mm)"])
            xespecie[peng["Species"]] += 1
    
        else:
            avculmendepth[peng["Species"]] = float(peng["Culmen Depth(mm)"])
            xespecie[peng["Species"]] = 1


    for esp,culmen in avculmendepth.items():
        avculmendepth[esp] = culmen/xespecie[esp]

    return avculmendepth

#media de la aleta(flipper) x especia
@router.get("/penguins/avculmen/flipper")
async def avculmen_depth():
    database = "size"
    filter = {}
    project={
        "Species" : 1,"Flipper Lengt (mm)":1, "_id" : 0
        }
    penguin_db = get_data(database, filter,project)
    avflipper = {}#guarda la suma de los culmen
    xespecie = {}
   
    for peng in penguin_db:
        if peng["Species"] in list(avflipper.keys()):
            avflipper[peng["Species"]] += float(peng["Flipper Lengt (mm)"])
            xespecie[peng["Species"]] += 1
    
        else:
            avflipper[peng["Species"]] = float(peng["Flipper Lengt (mm)"])
            xespecie[peng["Species"]] = 1


    for esp,fliper in avflipper.items():
        avflipper[esp] = fliper/xespecie[esp]

    return avflipper

#media del body
@router.get("/penguins/avbody/mass")
async def avculmen_depth():
    database = "size"
    filter = {}
    project={
        "Species" : 1,"Body Mass (gr)":1, "_id" : 0
        }
    penguin_db = get_data(database, filter,project)
    avbody = {}#guarda la suma de los culmen
    xespecie = {}
   
    for peng in penguin_db:
        if peng["Species"] in list(avbody.keys()):
            avbody[peng["Species"]] += float(peng["Body Mass (gr)"])
            xespecie[peng["Species"]] += 1
    
        else:
            avbody[peng["Species"]] = float(peng["Body Mass (gr)"])
            xespecie[peng["Species"]] = 1


    for esp,body in avbody.items():
        avbody[esp] = body/xespecie[esp]

    return avbody


@router.get("/penguins/island/latlong")
async def lat_long():
    database = "size"
    filter = {}
    project={
        "Island" : 1,"lat.long":1, "_id" : 0
        }
    penguin_db = get_data(database, filter,project)
    coor = {}#guarda la suma de los culmen
    for peng in project:
        if not peng['Island'] in coor.keys():
            coor[peng['Island']]= peng['lat']['long']
        
    return coor

