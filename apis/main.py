from flask import Blueprint
from flask_restplus import Api, Resource
from core import db
from core.models import Customer, Vendor
from core.modelSchema import CustomerSchema, VendorSchema
from marshmallow import ValidationError


home = Blueprint('home', __name__)
api = Api(home)


@api.route("/")
class Home(Resource):
    def get(self):
        return " "


@api.route("/register/vendor")
class Register_vendor(Resource):

    def post(self):
        vSchema = VendorSchema()
        try:
            vendor = vSchema.load(api.payload)
            new_vendor = Vendor(name=vendor["name"], password=vendor["password"],
                                location=vendor["location"],
                                Email=vendor["Email"],
                                company_number=vendor["company_number"])

            db.session.add(new_vendor)
            db.commit(new_vendor)
            return ({
                "message": f"Account created"
            }, 201)
        except ValidationError as err:
            return {"message": err}


@api.route("/register/user")
class Register_user(Resource):

    def post(self):
        cSchema = CustomerSchema()
        try:
            customer = cSchema.load(api.payload)
            new_customer = Customer(first_name=customer["first_name"],
                                    last_name=customer["last_name"],
                                    password=customer["password"],
                                    Address=customer["Address"],
                                    Email=customer["Email"],
                                    phone_number=customer["phone_number"])
            db.session.add(new_customer)
            db.session.commit()
            return ({
                "message": f"User account create successfully, welcome {customer['first_name']}"
            }, 201)
        except ValidationError as err:
            return {"message": err.messages}
