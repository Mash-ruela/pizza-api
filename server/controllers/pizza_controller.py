from flask import Blueprint, make_response, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return make_response(jsonify([p.to_dict() for p in pizzas]), 200)