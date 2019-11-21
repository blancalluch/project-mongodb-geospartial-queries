import os
import requests
from dotenv import load_dotenv
load_dotenv()
import json

def googleRequestAuthorized(address):
    '''Requesting google geocode API for information of a address'''
    authToken = os.getenv("API_KEY")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    else:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={authToken}"
        res = requests.get(url)

    return res

def apicompanies(ad):
    '''searches for the coordinates of that address'''
    loc_comp = googleRequestAuthorized(ad).json()
    return loc_comp