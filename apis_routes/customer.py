from flask import Blueprint
from core import db
from core.models import Customer, Order
from flask_restplus import Api, Resource
from core.modelSchema import CustomerSchema, OrderSchema

customer = Blueprint('customers', __name__)
api = Api(customer)


@api.route("/<user>")
class Account(Resource):
    def get(self):
        return " "

    def put(self):
        pass

    def delete(self):
        pass


@api.route("/orders")
class Orders(Resource):
    def get(self):
        oSchema = OrderSchema()
        order = Customer.query.all()
        orders = oSchema.dump(order)
        return orders

    def post(self):
        pass

    def delete(self):
        pass
