from server.config import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class RestaurantPizza(db.Model, SerializerMixin):
    _tablename_ = 'restaurant_pizzas'

    # Serialization rules to include related pizza and restaurant details
    serialize_rules = ('-pizza.restaurant_pizzas', '-restaurant.restaurant_pizzas')

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    # Relationships
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, price):
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30.")
        return price

    def _repr_(self):
        return f'<RestaurantPizza {self.id} Price: {self.price}>'