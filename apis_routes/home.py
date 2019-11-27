from flask import Blueprint
from elasticsearch import Elasticsearch
from flask_restplus import Api, Resource
from core.models import Category, Product, Customer, Vendor
from core.modelSchema import (CategorySchema, ProductSchema, LoginSchema)
                              # CustomerSchema, VendorSchema)
from utilities.utils import login_user as lg
from concurrent.futures import ThreadPoolExecutor
# from marshmallow import ValidationError


home = Blueprint('home', __name__)
api = Api(home)


@api.route("/home")
class Home(Resource):
    def get(self):
        cSchema = CategorySchema(many=True)
        pSchema = ProductSchema(many=True)
        products = Product.query.all()
        categories = Category.query.all()

        products = pSchema.dump(products)
        categories = cSchema.dump(categories)

        return {
            "products": products,
            " categories": categories
        }


@api.route("/login")
class Login(Resource):
    def post(self):
        lSchema = LoginSchema()
        user = lSchema.load(api.load)

        with ThreadPoolExecutor() as executor:
            check_u = executor.submit(lg, Customer, user)
        with ThreadPoolExecutor() as executor:
            check_v = executor.submit(lg, Vendor, user)

        if check_u.result is not None:
            # cSchema = CustomerSchema()
            # user = cSchema.dump(check_u.result)
            return {"message": "welcome"}, 200

        elif check_v.result is not None:
            # vSchema = VendorSchema()
            # user = vSchema.dump(check_v.result)
            return {"message": "welcome"}, 200

        else:
            return {"message": "invalid username or password"}, 404

    # for searching through the database with elastic search.


@api.route("/search")
class Search(Resource):
    def get(self):
        pass


@api.route("/<category>/products")
class CategoryProducts(Resource):
    def get(self, category):
        pSchema = ProductSchema(many=True)
        products = Product.query.get(category=category).paginate(per_page=10)

        products = pSchema.dump(products)
        return {
            "products": products,
        }
