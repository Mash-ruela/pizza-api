from flask import Blueprint, Flask, make_response, jsonify
from server.config import app
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

# Register Blueprints
app.register_blueprint(restaurant_bp, url_prefix='/')
app.register_blueprint(pizza_bp, url_prefix='/')
app.register_blueprint(restaurant_pizza_bp, url_prefix='/')

# Default route
@app.route('/')
def index():
    return "<h1>Pizza Restaurant API</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)