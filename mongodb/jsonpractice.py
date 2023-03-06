import json
from pymongo import MongoClient

client = MongoClient(host="172.17.0.2", port=27017)
db = client.geojson_flask
geodata_collection = db.geodata_collection

with open("points.geojson") as f:
  data = json.load(f)

#print(data["features"][0]["properties"]["name"])

# for i in range(len(data["features"])):
#   print(data["features"][i]["geometry"]["coordinates"])

for i in range(len(data["features"])):
    geodata_collection.insert_one({
         "type": "Feature",
         "properties": data["features"][i]["properties"]["name"],
         "geometry": {
         "type": "Point",
         "coordinates": data["features"][i]["geometry"]["coordinates"]
        }
    })

#print(addresses.find({"type": "'Point"}))
for feature in geodata_collection.find({}):
  print(feature["properties"])

# geodata_collection.delete_many({})
# print(geodata_collection.count_documents({}))