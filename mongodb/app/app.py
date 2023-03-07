# https://belmoussaoui.com/blog/5-display-geojson-data-using-flask-and-mongodb/
# install mongo db: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/

from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient(host="mongodb://mongo", port=27017)
db = client.geojson_flask
geodata_collection = db.geodata_collection

# client = MongoClient("mongodb://localhost:27017/")
# db = client["mydatabase"]
# addresses = db["addresses_collection"]

# Read GeoJSON file from local system
# with open("points.geojson") as f:
#   data = json.load(f)



# @app.route('/geojson-features', methods=['GET'])
# def get_all_points():
#     features = []
#     for geo_feature in geodata_collection.find({}):
#         features.append({
#             "type": "FeatureCollection",
#             "geometry": {
#                 "type": geo_feature['geometry']['type'],
#                 "coordinates": geo_feature['geometry']['coordinates']
#             }
#         })
#     return jsonify(features)

# for feature in geodata_collection.find({}):
#   print(feature['geometry']['coordinates'])

@app.route('/points', methods=['GET'])
def get_all_points():
    features = []
    geojson ={
        "features":[]
    }
    for geo_feature in geodata_collection.find({}):
        features.append({
            "type": "Feature",
            "properties": geo_feature["properties"],
            "geometry": {
                "type": geo_feature["geometry"]["type"],
                "coordinates": geo_feature["geometry"]["coordinates"]
            }
        })
        
    geojson["features"] = features
    return jsonify(geojson)

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)