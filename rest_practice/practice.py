# JSONPlaceholder: free service provides fake API endpoints that send back responses that requests can process. https://jsonplaceholder.typicode.com/

import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos/1"

# GET request
print('GET request')
response = requests.get(api_url)
print(response.json())
print(response.status_code)
print(response.headers["Content-Type"])

# POST request. 
api_url = "https://jsonplaceholder.typicode.com/todos/"
todo = {
    "userId": 1,
    "title": "Buy milk",
    "completed": False
}
response = requests.post(api_url, json=todo)

# we can also set the headers to serialize the JSON manually
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print('POST request')
print(response.json())
print(response.status_code)

# PUT request. PUT request to update an existing todo with new data
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print('GET request for item 10')
print(response.json())

todo = {"userId": 1, "title": "Wash car", "completed": True}
print('PUT request')
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)

# PATCH request  modify the value of a specific field on an existing todo. 
# PATCH differs from PUT in that it doesn’t completely replace the existing resource. 
# It only modifies the values set in the JSON sent with the request.
api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
print('PATCH request to modifty exsiting record')
response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)

# DELETE request
api_url = "https://jsonplaceholder.typicode.com/todos/10"
print('DELETE 10th item')
response = requests.delete(api_url)
print(response.json())
print(response.status_code)

