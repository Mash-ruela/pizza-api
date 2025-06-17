from server.config import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        print("Clearing old data...")
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()
        db.session.commit()

        print("Seeding new data...")

        # Seed Restaurants
        restaurants = [
            Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201"),
            Restaurant(name="Pizzeria Mozza", address="641 N Highland Ave, Los Angeles, CA 90036"),
            Restaurant(name="Kiki's Pizza", address="123 Pizza Ln, Foodie Town, USA")
        ]
        db.session.add_all(restaurants)
        db.session.commit()

        # Seed Pizzas
        pizzas = [
            Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
            Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil"),
            Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese, Olives, Green Peppers")
        ]
        db.session.add_all(pizzas)
        db.session.commit()

        # Seed RestaurantPizzas (Associations)
        restaurant_pizzas = [
            RestaurantPizza(price=15, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=18, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=20, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=5, restaurant_id=3, pizza_id=1)
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Seeding complete! ✅")

if __name__ == '__main__':
    seed_data()