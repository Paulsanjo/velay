from flask import Blueprint
from core import db
from flask_restplus import Api, Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from core.models import Customer, Order, Review, Vendor
from core.modelSchema import CustomerSchema, OrderSchema, ReviewSchema


customer = Blueprint('customers', __name__)
api = Api(customer)


@api.route("/register/user")
class Register_user(Resource):

    def post(self):
        cSchema = CustomerSchema()
        try:
            customer = cSchema.load(api.payload)
            check = Customer.query.filter_by(Email=customer["Email"]).first()
            check2 = Vendor.query.filter_by(Email=customer["Email"]).first()
            if not check or check2:
                try:
                    new_customer = Customer(first_name=customer["first_name"],
                                            last_name=customer["last_name"],
                                            password=customer["password"],
                                            Address=customer["Address"],
                                            Email=customer["Email"],
                                            phone_number=customer["phone_number"])
                    # db.session.add(new_customer)
                    # db.session.commit()
                    return ({"message": f"User account create successfully, welcome"}, 201)
                except Exception:
                    # db.session.rollback()
                    return{"phone_error": "phone number already in use, pick another"}, 400
            raise ValidationError("Email already taken, use a different email")
        except ValidationError as err:
            return {"other_error": err.messages}


@api.route("/user/<name>")
class Account(Resource):
    def get(self, name):
        return " "

    def put(self, name):
        pass

    def delete(self, name):
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


@api.route("/vendor/<vendor>/product/<int:product_id>/review")
class ProductReview(Resource):
    def get(self):
        reviews = Review.get().paginate(per_page=10)
        rSchema = ReviewSchema()
        results = rSchema.dump(reviews, many=True)
        return {"reviews": results}

    def post(self):
        # asynchronous function for posting reviews to the site
        rSchema = ReviewSchema()
        review = rSchema.load(api.payload)
        try:
            if review:
                new_review = Review(
                    review["rating"],
                    review["title"],
                    review["content"]
                )
                db.session.add(new_review)
                db.session.commit()
                return {"message": "Thank you for reviewing this product"}
        except IntegrityError:
            db.session.rollback()
            return {"error": "Invalid entry, please try again"}, 500


@api.route("/<vendor>/product/<int:product_id>/review/<int:review_id>")
class Review_OneProduct(Resource):
    def get(self, review_id):
        review = Review.query.get_or_404(id=review_id).first()
        rSchema = ReviewSchema()
        results = rSchema.dump(review)
        return {"reviews": results}

    def delete(self, review_id):
        review = Review.query.get_or_404(id=review_id).first()
        db.session.delete(review)
        db.session.commit()
        return {"message": "successfully deleted item"}, 203
