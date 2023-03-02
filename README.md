# REST_APIs
[RESTful web API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#uri-versioning).  

First identify the resources the API will manage. Use plural nouns. Also consider nested resource hierarchies. Like transations and then transations/<transation_id>  
Endpoint should never contain verbs. 

|HTTP method|API endpoint|Description|
|:----|:----|:----|
|GET|/transactions|Get a list of transactions.|
|GET|/transactions/<transaction_id>|Get a single transaction.|
|POST|/transactions|Create a new transaction.|
|PUT|/transactions/<transaction_id>|Update a transaction.|
|PATCH|/transactions/<transaction_id>|Partially update a transaction.|
|DELETE|/transactions/<transaction_id>|Delete a transaction.|  

Here is an example of a nested resource: 


|HTTP method|API endpoint|Description|
|:----|:----|:----|
|GET|/events/<event_id>/guests|Get a list of guests.|
|GET|/events/<event_id>/guests/<guest_id>|Get a single guest.|
|POST|/events/<event_id>/guests|Create a new guest.|
|PUT|/events/<event_id>/guests/<guest_id>|Update a guest.|
|PATCH|/events/<event_id>/guests/<guest_id>|Partially update a guest.|
|DELETE|/events/<event_id>/guests/<guest_id>|Delete a guest.|

We can also use query strings. Here we append a query string to get guests for a specific event_id:

```HTTP
GET /guests?event_id=23
```
For the tutorial, here is the API design:  
|Action|HTTP Verb|URL Path|Description|
|:----|:----|:----|:----|
|Read|GET|/api/people|Read a collection of people.|
|Create|POST|/api/people|Create a new person.|
|Read|GET|/api/people/<lname>|Read a particular person.|
|Update|PUT|/api/people/<lname>|Update an existing person.|
|Delete|DELETE|/api/people/<lname>|Delete an existing person.|  

The Connexion module allows a Python program to use the OpenAPI specification with Swagger. The OpenAPI Specification is an API description format for REST APIs and provides a lot of functionality,  including:
  - Validation of input and output data to and from your API  
  - Configuration of the API URL endpoints and the expected parameters  

For the swagger.yml file, here are the object types:  
- string: A string type
-number: Numbers supported by Python (integers, floats, longs)
- object: A JSON object, which is roughly equivalent to a Python dictionary
- array: Roughly equivalent to a Python List
- boolean: Represented in JSON as true or false, but in Python as True or False
- null: Essentially None in Python

Marshmallow helps you to create a PersonSchema class, which is like the SQLAlchemy Person class you just created. The PersonSchema class defines how the attributes of a class will be converted into JSON-friendly formats. Marshmallow also makes sure that all attributes are present and contain the expected data type.  










