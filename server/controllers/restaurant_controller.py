from flask import Blueprint, make_response, jsonify
from server.models.restaurant import Restaurant, db
from server.models.pizza import Pizza

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return make_response(jsonify([r.to_dict(rules=('-restaurant_pizzas',)) for r in restaurants]), 200)

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)
    
    # Manually build the response to include pizzas
    restaurant_data = restaurant.to_dict(rules=('-restaurant_pizzas',))
    pizzas = [rp.pizza.to_dict(rules=('-restaurant_pizzas',)) for rp in restaurant.restaurant_pizzas]
    restaurant_data['pizzas'] = pizzas
    
    return make_response(jsonify(restaurant_data), 200)

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)
    
    db.session.delete(restaurant)
    db.session.commit()
    
    return make_response('', 204)