import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()


def googleSearch(googleSearchObject : str):
    string = "https://www.googleapis.com/customsearch/v1?key=" + os.getenv('GoogleCustomSearch') + "&cx=" + os.getenv('searchEngineId') + "&q="+ googleSearchObject

    res = requests.get(str(string))
    response = json.loads(res.text).get('items')

    links = []

    for i in response:
        links.append(i.get('link'))

    return links