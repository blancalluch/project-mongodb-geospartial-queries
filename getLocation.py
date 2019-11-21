def getLocation(long,lat):
    '''Creates a dictionary in the format of mongo db geolocations'''
    loc = {
        'type':'Point',
        'coordinates':[float(long), float(lat)]
    }
    return loc