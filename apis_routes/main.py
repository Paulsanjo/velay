from flask import Blueprint, request
from flask_restplus import Api, Resource
from core.models import Product, Review
from core.modelSchema import ProductSchema
# from marshmallow import ValidationError


home = Blueprint('home', __name__)
api = Api(home)


@api.route("/")
class Home(Resource):
    def get(self):
        pSchema = ProductSchema(many=True)
        page = request.args.get("page", 1, type=int)
        product = Product.query.order_by(Review.rating.asc()).paginate(page=page, per_page=12)
        product = pSchema.dump(product.items)
        return {"product": product}


@api.route("/login")
class Login(Resource):
    def post(self):
        return " "

# for searching through the database with elastic search.


@api.route("/search")
class Search(Resource):
    def get(self):
        return " "
