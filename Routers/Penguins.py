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

#todas las especies como hago que me aparazcan solo las 3
@router.get("/species")
async def species():
    res = get_data("size", {}, {"Species":1, "_id": 0})
    species = []
    for peng in res:
        species.append(peng["Species"])
    species.sort()
    return list(set(species))

#todas las islas como hago que me aparazcan solo las 3
@router.get("/islands")
async def players_all_name():
    res = get_data("size", {}, {"Island":1, "_id": 0})
    all_islands = []
    for peng in res:
        all_islands.append(peng["Island"])
    all_islands.sort()
    return list(set(all_islands))



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

@router.get("/penguins/avculmen/flipper/{sex}")
async def flipperxsex(sex):
    database = "size"
    filter = {"Sex": sex}
    project={
        "Species" : 1,"Flipper Lengt (mm)":1,"Sex": 1, "_id" : 0
        }
    penguin_db = get_data(database, filter,project)    
    sexflipper = {}#guarda la suma de los culmen
    xespecie = {}
   
    for peng in penguin_db:
        if peng["Species"] + peng["Sex"] in list(sexflipper.keys()):
            sexflipper[peng["Species"]+ peng["Sex"]] += float(peng["Flipper Lengt (mm)"])
            xespecie[peng["Species"] + peng["Sex"] ] += 1

        else:
            sexflipper[peng["Species"]+ peng["Sex"]] = float(peng["Flipper Lengt (mm)"])
            xespecie[peng["Species"] + peng["Sex"] ] = 1   


    for esp,fliper in sexflipper.items():
        sexflipper[esp] = fliper/xespecie[esp]        

    return sexflipper

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


@router.get("/penguins/latlong/{island}")
async def lat_long(island):
    database = "size"
    res = get_data(database, {"Island":island}, {"Island Longitude":1},{"Island Latitude":1}, {"_id":0})
    return loads(json_util.dumps(res[0]))
