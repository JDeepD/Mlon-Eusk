import random
import json
import requests


with open(r'apis/creds/creds.json', 'r') as logins:
    api_key = json.load(logins)["giphyapi"]['api_key']

def getgif(query):
    qu = '+'.join(query.split(" "))
    print(qu)
    url = f"http://api.giphy.com/v1/gifs/search?q={qu}&api_key={api_key}"
    jsdata = requests.get(url)
    data = json.loads(jsdata.content)
    print(len(data['data']))
    print(data['data'][random.randint(0, 49)]['url'])
    return data['data'][random.randint(0, 49)]['url']


getgif("naruto")



