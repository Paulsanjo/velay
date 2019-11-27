from flask import Blueprint
from core import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from flask_restplus import Api, Resource
from core.models import Product, Vendor, Customer
from core.modelSchema import ProductSchema, VendorSchema

vendor = Blueprint('vendors', __name__)
api = Api(vendor)


@api.route("/register/vendor")
class Register_vendor(Resource):

    def post(self):
        vSchema = VendorSchema()
        try:
            vendor = vSchema.load(api.payload)
            check = Vendor.query.filter_by(Email=vendor["Email"]).first()
            if not check:
                try:
                    new_vendor = Vendor(name=vendor["name"], password=vendor["password"],
                                        location=vendor["location"],
                                        Email=vendor["Email"],
                                        company_number=vendor["company_number"])

                    db.session.add(new_vendor)
                    db.commit(new_vendor)
                    return ({
                        "message": f"Account created"
                    }, 201)
                except IntegrityError:
                    db.session.rollback()
                    return{"message": "phone number already exists select a different one"}
            else:
                return {"message": "Email already exists select a different one"}
        except ValidationError as err:
            return {"message": err.message}


@api.route("/vendor/<vendor>")
class Account(Resource):
    def get(self, vendor):
        pass

    def put(self, vendor):
        pass

    def delete(self, vendor):
        pass


@api.route("/vendor/<vendor>/product")
class Products(Resource):
    def get(self):
        pass

    def post(self):
        pass


@api.route("/vendor/<vendor>/product/<int:product_id>")
class SpecificProduct(Resource):
    def get(self, product_id):
        pass

    def put(self, product_id):
        pass

    def delete(self, product_id):
        pass
