import json
from requests import get

with open('creds/creds.json', 'r') as logins:
    api_key = json.load(logins)["nasaapi"]['api_key']


def apod():
    jsdat = get(f"https://api.nasa.gov/planetary/apod/?api_key={api_key}")
    data = json.loads(jsdat.content)
    return (data["title"], data['explanation'], data["url"])


"""Deprecated"""
def imagery():
    jsdat = get(f"https://api.nasa.gov/planetary/earth/imagery/?api_key={api_key}")
    data = json.loads(jsdat.content)
    return data

print(apod())
