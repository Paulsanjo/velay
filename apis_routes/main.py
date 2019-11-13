from flask import Blueprint, request
from flask_restplus import Api, Resource
from core import db
from core.models import Customer, Vendor, Product, Review
from core.modelSchema import CustomerSchema, VendorSchema, ProductSchema
from marshmallow import ValidationError


home = Blueprint('home', __name__)
api = Api(home)


@api.route("/")
class Home(Resource):
    def get(self):
        pSchema = ProductSchema()
        page = request.args.get("page", 1, type=int)
        product = Product.query.order_by(Review.rating.asc()).paginate(page=page, per_page=12)
        product = pSchema.dump(product.items, many=True)
        return {"product": product}


@api.route("/register/vendor")
class Register_vendor(Resource):

    def post(self):
        vSchema = VendorSchema()
        try:
            vendor = vSchema.load(api.payload)
            check = Vendor.query.filter_by(Email=vendor["Email"]).first()
            if not check:
                new_vendor = Vendor(name=vendor["name"], password=vendor["password"],
                                    location=vendor["location"],
                                    Email=vendor["Email"],
                                    company_number=vendor["company_number"])

                db.session.add(new_vendor)
                db.commit(new_vendor)
                return ({
                    "message": f"Account created"
                }, 201)
            else:
                return {"message": "Email or phone number already exists select a different one"}
        except ValidationError as err:
            return {"message": err.message}


@api.route("/register/user")
class Register_user(Resource):

    def post(self):
        cSchema = CustomerSchema()
        try:
            customer = cSchema.load(api.payload)
            check = Customer.query.filter_by(Email=customer["Email"]).first()
            if not check:
                new_customer = Customer(first_name=customer["first_name"],
                                        last_name=customer["last_name"],
                                        password=customer["password"],
                                        Address=customer["Address"],
                                        Email=customer["Email"],
                                        phone_number=customer["phone_number"])
                # db.session.add(new_customer)
                # db.session.commit()
                return ({
                    "message": f"User account create successfully, welcome {customer['first_name']}"
                }, 201)
            raise ValidationError("Email already taken, use a different email")
        except ValidationError as err:
            return {"message": err.messages}
