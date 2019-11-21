from pymongo import MongoClient
import os
import requests
from dotenv import load_dotenv
load_dotenv()
import json

def getLocation(long,lat):
    '''Creates a dictionary in the format of mongo db geolocations'''
    loc = {
        'type':'Point',
        'coordinates':[float(long), float(lat)]
    }
    return loc

def connectCollection(database, collection):
    '''Connecting with mongoDB and reading database collection.'''
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll

def googleRequestAuthorized(address):
    '''Requesting google geocode API for information of a address'''
    authToken = os.getenv("API_KEY")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    else:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={authToken}"
        res = requests.get(url)

    return res

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

def geoquery(coll,coordinates,radius):
    '''calculates the objects from a collection that are near the coordinates '''
    sol=coll.find(
    {"location":
     {"$near":
      {"$geometry":
       {"type":"Point",
        "coordinates":coordinates
       },
       "$maxDistance":radius
      }
     }
    }
)
    return sol

def googleNearBy_RequestAuthorized(params):
    '''Requesting google geocode API for information of a address'''
    authToken = os.getenv("API_KEY")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    else:
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?{params}"
        res = requests.get(url)

    return res