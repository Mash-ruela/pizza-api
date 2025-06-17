from flask import Blueprint, request, make_response, jsonify
from server.models.restaurant_pizza import RestaurantPizza, db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Verify that the pizza and restaurant exist
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return make_response(jsonify({"errors": ["Pizza or Restaurant not found"]}), 404)

    try:
        new_restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        
        # Manually build the response to match the required format
        response_data = new_restaurant_pizza.to_dict(rules=('-pizza', '-restaurant'))
        response_data['pizza'] = pizza.to_dict(rules=('-restaurant_pizzas',))
        response_data['restaurant'] = restaurant.to_dict(rules=('-restaurant_pizzas',))

        return make_response(jsonify(response_data), 201)

    except ValueError as e:
        return make_response(jsonify({"errors": [str(e)]}), 400)
    except Exception:
        return make_response(jsonify({"errors": ["Validation errors"]}), 400)