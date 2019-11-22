def getLatAirport(row):
    return getCoordAirport(row)[1]

def getLongAirport(row):
    return getCoordAirport(row)[0]

def getCoordAirport(row):
    return row['airports'][0]['location']['coordinates']