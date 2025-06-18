# 🍕 Pizza API Challenge

A Flask-based RESTful API for managing restaurants, pizzas, and their associations.

GitHub: [https://github.com/Mash-ruela/pizza-api.git](https://github.com/Mash-ruela/pizza-api.git)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Mash-ruela/pizza-api.git
cd pizza-api

### 2. Create Virtual Environment
```bash
pipenv install
pipenv shell

--if pipenv is not installed
```bash
pip install pipenv

### 3. Install Additional Packages (if not already installed)
```bash
pipenv install flask flask-sqlalchemy flask-migrate sqlalchemy-serializer

## Database Setup

###1. Initialize Migrations
```bash
flask --app server.app db init

###2. Generate Migration
```bash
flask --app server.app db migrate -m "Initial migration"

###3. Apply Migration
```bash
flask --app server.app db upgrade

###4. Seed the Database
```bash
pipenv run python seed.py

###🚀 Running the Server
```bash
flask --app server.app run --port=5555

--The server runs at: http://127.0.0.1:5555

##📦 Routes Summary
Method	Route	Description
GET	/	-- Welcome route
GET	/pizzas	-- Get all pizzas
GET	/restaurants	-- Get all restaurants
GET	/restaurants/<id>	-- Get a specific restaurant with its pizzas
POST	/restaurant_pizzas	-- Add a pizza to a restaurant
DELETE	/restaurants/<id>	-- Delete a restaurant

##Example Requests & Responses
GET /pizzas
Response:
--
json
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  }
]

GET /restaurants/1
Response:

json
{
  "id": 1,
  "name": "Sottocasa NYC",
  "address": "298 Atlantic Ave, Brooklyn, NY 11201",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    }
  ]
}

POST /restaurant_pizzas
Request:

json
{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 1
}

Response (201 Created):

json
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
DELETE /restaurants/3
Response:

json
{
  "message": "Restaurant deleted"
}

##✅ Validation Rules
POST /restaurant_pizzas:

price: must be an integer between 1 and 30.

pizza_id and restaurant_id: must reference valid existing records.

Invalid data will return a 400 status with an error message.

Example Error Response:

json
{
  "errors": ["Price must be between 1 and 30"]
}

### Using Postman
Open Postman and Import the collection:

File name: challenge-1-pizzas.postman_collection.json

Collection includes pre-configured requests for all endpoints.

Start your Flask server:

```bash
flask --app server.app run
Use the collection to send requests to:

cpp
http://127.0.0.1:5555
Make sure your Flask server is running before using Postman!

👩🏽‍💻 Author
Ruth Macharia