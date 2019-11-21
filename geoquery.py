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