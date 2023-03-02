# set env variables
# export FLASK_APP=app.py
# export FLASK_ENV=development

from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/countries/<int:id>")
def get_country(id):
   
    # find the country with the given id
    country = next((c for c in countries if c["id"] == id), None)
    # if the country exists, return it as JSON
    if country:
        return jsonify(country)
    # otherwise, raise an IndexError
    else:
        raise IndexError("Country not found")
   
        
    
    # return jsonify(countries[id])

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

