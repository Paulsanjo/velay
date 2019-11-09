from flask import Blueprint
from core import db
from flask_restplus import Api, Resource
from core.modelSchema import ProductSchema, ReviewSchema, VendorSchema

vendors = Blueprint('vendors', __name__)
api = Api(vendors)


@api.route("/<vendor>")
class Account(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


@api.route("/<vendor>/product")
class Products(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


@api.route("/<vendor>/review")
class Review(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
