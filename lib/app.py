from flask import Flask, jsonify, request
from models import db, migrate, Restaurant, Pizza, RestaurantPizza
from wtforms.validators import ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RestaurantAPI.db'
db.init_app(app)
migrate.init_app(app, db)

# Routes

# GET all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
    return jsonify(result)

# GET a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = [{"id": restaurant_pizza.pizza.id, "name": restaurant_pizza.pizza.name, "ingredients": restaurant_pizza.pizza.ingredients} for restaurant_pizza in restaurant.restaurant_pizzas]
        result = {"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "pizzas": pizzas}
        return jsonify(result)
    return jsonify({"error": "Restaurant not found"}), 404


# DELETE a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        # Cascade delete to related RestaurantPizza records
        for restaurant_pizza in restaurant.restaurant_pizzas:
            db.session.delete(restaurant_pizza)
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Restaurant not found"}), 404


# GET all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
    return jsonify(result)

# POST a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = float(data["price"])
    pizza_id = int(data["pizza_id"])
    restaurant_id = int(data["restaurant_id"])

    try:
        # Validate price range
        if not (1 <= price <= 30):
            raise ValidationError("Price must be between 1 and 30.")

        # Check if Pizza and Restaurant exist
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if pizza and restaurant:
            restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
            db.session.add(restaurant_pizza)
            db.session.commit()
            return jsonify({"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}), 201

        return jsonify({"error": "Pizza or Restaurant not found"}), 404

    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
