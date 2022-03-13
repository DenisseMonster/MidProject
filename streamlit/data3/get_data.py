import requests

url = "http://127.0.0.1:8000"

def islandpop():
    return requests.get(url+"/penguins/islandpop").json()

def avculmen():
    return requests.get(url+"/penguins/avculmen/length").json()

def avdepth():
    return requests.get(url+"/penguins/avculmen/depth").json()

def avflipper():
    return requests.get(url+"/penguins/avculmen/flipper").json()

def avbody():
    return requests.get(url+"/penguins/avbody/mass").json()