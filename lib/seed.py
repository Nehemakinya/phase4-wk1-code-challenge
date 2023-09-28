from app import app, db
from models import Restaurant, Pizza, RestaurantPizza


def create_restaurants():
    restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")
    
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.commit()

def create_pizzas():
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.commit()

def create_restaurant_pizzas():
    restaurant1 = Restaurant.query.filter_by(name="Dominion Pizza").first()
    restaurant2 = Restaurant.query.filter_by(name="Pizza Hut").first()
    
    pizza1 = Pizza.query.filter_by(name="Cheese").first()
    pizza2 = Pizza.query.filter_by(name="Pepperoni").first()
    
    restaurant_pizza1 = RestaurantPizza(price=10.0, pizza=pizza1, restaurant=restaurant1)
    restaurant_pizza2 = RestaurantPizza(price=12.0, pizza=pizza2, restaurant=restaurant1)
    restaurant_pizza3 = RestaurantPizza(price=11.0, pizza=pizza1, restaurant=restaurant2)
    
    db.session.add(restaurant_pizza1)
    db.session.add(restaurant_pizza2)
    db.session.add(restaurant_pizza3)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        create_restaurants()
        create_pizzas()
        create_restaurant_pizzas()
        print("Data seeded successfully.")
