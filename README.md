# flask-sqlite-api
Backend service with two API endpoints for storing information about a boat and retrieving the closest 5 boats


## Steps to get service running
1. Download Github Repository
2. Open Terminal 
2. Execute the following command in terminal
```
	./run.sh
```

## CURL Examples

### Retrieve Endpoint 
The following CURL command will retrieve the 5 closest boats, given a latitude/longitude that is provided.
```
curl http://localhost:5000/retrieve\?latitude=1.1\&longitude=1.1
```

### Store Endpoint 
The following CURL command will store information about a boat including make, model, length, latitude, longitude

```
curl -X POST -H "Content-Type: application/json" -d '{
  "latitude": 40.7128,
  "longitude": 74.0060,
  "make":"Boston Whaler",
  "model":"Outrage 19,4",
  "length":19
}' http://localhost:5000/store

curl -X POST -H "Content-Type: application/json" -d '{
  "latitude": 25.7617,
  "longitude": 80.1918,
  "make":"Little Harbor",
  "model":"Blackwatch 36 Express",
  "length":36
}' http://localhost:5000/store

curl -X POST -H "Content-Type: application/json" -d '{
  "latitude": 41.8781,
  "longitude": 87.6298,
  "make":"Bristol",
  "model":"45.5",
  "length":45
}' http://localhost:5000/store

curl -X POST -H "Content-Type: application/json" -d '{
  "latitude": 37.7749,
  "longitude": 122.4194,
  "make":"Bayliner",
  "model":"2855",
  "length":29
}' http://localhost:5000/store


curl -X POST -H "Content-Type: application/json" -d '{
  "latitude": 39.9526,
  "longitude": 75.1652,
  "make":"Ericson",
  "model":"30+",
  "length":30
}' http://localhost:5000/store

curl -X POST -H "Content-Type: application/json" -d '{
  "latitude": 33.7490,
  "longitude": 84.3880,
  "make":"Kadey Krogen",
  "model":"Kadey Krogen 38",
  "length":38
}' http://localhost:5000/store

```

## Next Steps (if had more time)
1. Dockerize Flask Application to more easily deploy to cloud and run in different environments 
2. Implement unit testing with pytest-flask
3. Utilize Marshmallow Python library to serialize and deserialize data through endpoints
4. Provide additional documentation across functions and classes
5. Implement logging for improved trouble shooting
6. Add authentication 