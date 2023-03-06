# https://realpython.com/introduction-to-mongodb-and-python/

import pymongo
from pymongo import MongoClient
import json
import pprint

# establish a connection
# client = MongoClient()
# to provide custom host, port use this: 
# client = MongoClient(host="localhost", port=27017)

client = MongoClient(host="172.17.0.2", port=27017) # this IP is the IP of the docker with mongo in it. 

# This is the MongoDB URL format:
# client = MongoClient("mongodb://localhost:27017")

db = client.rptutorials
# also can use when name of databse is not a valid idetifier: db = client["rptutorials"]

# a document
tutorial1 = {
     "title": "Working With JSON Data in Python",
     "author": "Lucas",
     "contributors": [
         "Aldren",
         "Dan",
         "Joanna"
     ],
     "url": "https://realpython.com/python-json/"
}

# specify which collection you want to use
tutorial = db.tutorial
#result = tutorial.insert_one(tutorial1)
# insert many documents

tutorial2 = {
     "title": "Python's Requests Library (Guide)",
     "author": "Alex",
     "contributors": [
         "Aldren",
         "Brad",
         "Joanna"
     ],
     "url": "https://realpython.com/python-requests/"
}
tutorial3 = {
     "title": "Object-Oriented Programming (OOP) in Python 3",
     "author": "David",
     "contributors": [
         "Aldren",
         "Joanna",
         "Jacob"
     ],
     "url": "https://realpython.com/python3-object-oriented-programming/"
}

#new_result = tutorial.insert_many([tutorial2, tutorial3])
#print(f"Multiple tutorials: {new_result.inserted_ids}")



# Read GeoJSON file from local system
with open("points.geojson") as f:
  data = json.load(f)

tutorial.insert_many(data["features"])

# for doc in tutorial.find():
#      pprint.pprint(doc)

#cessna_tutorial = tutorial.find_one({"type": "Feature"})
#tutorial.delete_many({})
print(tutorial.count_documents({}))

client.close()