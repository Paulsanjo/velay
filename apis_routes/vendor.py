from flask import Blueprint, request
from core import db
from flask_restplus import Api, Resource
from core.models import Product, Vendor
from core.modelSchema import ProductSchema, VendorSchema

vendor = Blueprint('vendors', __name__)
api = Api(vendor)


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
