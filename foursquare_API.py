from pymongo import MongoClient
import os
import requests
from dotenv import load_dotenv
load_dotenv()
import json

def foursquareRequestAuthorized(params):
    '''Requesting foursquare API for the information of a place with specific requirements.'''
    authToken1 = os.getenv("CLIENT_ID")
    authToken2 = os.getenv("CLIENT_SECRET")
    if not authToken1 or not authToken2:
        raise ValueError("NECESITAS UN TOKEN")
    else:
        params["client_id"] = authToken1
        params["client_secret"] = authToken2
        url = 'https://api.foursquare.com/v2/venues/explore'
        res = requests.get(url, params=params)

    return res

def apifoursquare(long,lat,query,limit,radius):
    '''Foursquare API specific requirements(ex. radius:500m,limits:1 place, coordinates: (lat,long))'''
    location = {"v":"20180323",
               "ll":f'{lat},{long}',
               "query":"{query}",
               "limit":limit,
               "radius":radius}
    data = json.loads(foursquareRequestAuthorized(location).text)
    return data