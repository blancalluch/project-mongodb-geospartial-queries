def geoquery(coll,long,lat,radius):
    '''calculates the objects from a collection that are near the coordinates '''
    sol=coll.find(
    {"location":
     {"$near":
      {"$geometry":
       {"type":"Point",
        "coordinates":[long,lat]
       }, 
       "$maxDistance":radius
      }
     }
    }
).limit(1)
    return list(sol)