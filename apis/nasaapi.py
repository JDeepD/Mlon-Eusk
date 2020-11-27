import json
from requests import get

with open(r'apis/creds/creds.json', 'r') as logins:
    api_key = json.load(logins)["nasaapi"]['api_key']


def apod():  # pylint: disable=all
    jsdat = get(f"https://api.nasa.gov/planetary/apod/?api_key={api_key}")
    data = json.loads(jsdat.content)
    return (data["title"], data['explanation'], data["url"])


def imagery():
    """Deprecated"""
    jsdat = get(f"https://api.nasa.gov/planetary/earth/imagery/?api_key={api_key}")  # noqa
    data = json.loads(jsdat.content)
    return data
