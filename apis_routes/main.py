from flask import Blueprint
from flask_restplus import Api, Resource
from core.models import Category
from core.modelSchema import CategorySchema
# from marshmallow import ValidationError


home = Blueprint('homes', __name__)
api = Api(home)


@api.route("/")
class Home(Resource):
    def get(self):
        cSchema = CategorySchema(many=True)
        categories = Category.query.get().all()
        categories = cSchema.dump(categories)
        return {"Categories": categories}


@api.route("/login")
class Login(Resource):
    def post(self):
        return " "

# for searching through the database with elastic search.


@api.route("/search")
class Search(Resource):
    def get(self):
        return " "
