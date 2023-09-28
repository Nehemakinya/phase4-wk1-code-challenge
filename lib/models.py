from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# Define Restaurant model
class Restaurant(db.Model):
    __tablename__ = 'restaurants'  
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __init__(self, name, address):
        self.name = name
        self.address = address

# Define Pizza model
class Pizza(db.Model):
    __tablename__ = 'pizzas'  

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

# Define RestaurantPizza model
class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'  

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)

    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas', lazy=True))
    restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizzas', lazy=True))

    def __init__(self, price, pizza_id, restaurant_id):
        self.price = price
        self.pizza_id = pizza_id
        self.restaurant_id = restaurant_id
