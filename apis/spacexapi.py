"""This script will get data from the spacex api"""

import json
import requests


def latest(url="https://api.spacexdata.com/v4/launches/latest"):
    """This method will take in a url and make request
    to the spacex api"""

    req = requests.get(url).content
    return json.loads(req)
