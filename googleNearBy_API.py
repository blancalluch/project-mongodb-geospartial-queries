import os
import requests
from dotenv import load_dotenv
load_dotenv()
import json

def googleNearBy_RequestAuthorized(params):
    '''Requesting google geocode API for information of a address'''
    authToken = os.getenv("API_KEY")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    else:
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={authToken}&{params}"
        res = requests.get(url)

    return res

def placesearch(lat,long,radius,place):
    '''searches for a place near the coordinates in a radius x'''
    params=f"location={lat},{long}&radius={radius}&keyword={place}"
    loc_comp = googleNearBy_RequestAuthorized(params).json()
    return loc_comp