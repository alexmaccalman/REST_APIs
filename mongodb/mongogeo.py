# https://belmoussaoui.com/blog/5-display-geojson-data-using-flask-and-mongodb/


import json
from pymongo import MongoClient

# Connect to MongoDB server and get collection object
client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
collection = db.test_collection

# Create a JSON string with featureCollection data
json_string = '''
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [102.0, 0.5]
      },
      "properties": {
        "prop0": "value0"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [102.0, 0.0],
          [103.0, 1.0],
          [104.0, 0.0],
          [105.0, 1.0]
        ]
      },
      "properties": {
        "prop1": 0,
        "prop2": 10
      }
    }
  ]
}
'''

# Convert JSON string to a list of dictionaries
data = json.loads(json_string)
documents = data['features']

# Insert documents into collection using insert_many()
result = collection.insert_many(documents)

# Print the inserted ids
print(result.inserted_ids)