## Restaurant and Pizza API
This is a simple Flask application for managing restaurants and pizzas. It provides a RESTful API for creating, retrieving, and deleting restaurants and pizzas, as well as creating restaurant-pizza combinations.

# Getting Started
To get started with this application, follow the steps below:

# Prerequisites
Python (version 3.10.0)
Flask (version 2.3.3)
Flask-SQLAlchemy (version 2.5.1)
Flask-Migrate (version 3.1.0)
SQLite or another supported database

# Installation
1. Clone this repository to your local machine:

git clone https://github.com/Nehemakinya/restaurant-pizza-api.git

2. Navigate to the project directory:

cd phase4-wk1-code-challenge

3. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install the required dependencies:

pipenv install

5. Configure the database URI in the app.py file:

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RestaurantAPI.db'  # Update with your database URI

6. Initialize the database and apply migrations:

flask db init
flask db migrate
flask db upgrade
 
# Usage
1. Start the Flask application:

flask run

2. Access the API using the following endpoints:

GET /restaurants: Retrieve a list of all restaurants.
GET /restaurants/<int:id>: Retrieve a specific restaurant by ID.
DELETE /restaurants/<int:id>: Delete a restaurant by ID.
GET /pizzas: Retrieve a list of all pizzas.
POST /restaurant_pizzas: Create a new restaurant-pizza combination.


# Data Seeding
To populate the database with initial data, you use the seed.py script. Run it as follows:

python seed.py

# Acknowledgments
This project was created as a simple example of building a RESTful API with Flask and SQLAlchemy.


**Author:** Nehema Kinya.