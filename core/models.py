from core import db
from datetime import datetime


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    Address = db.Column(db.String(50))
    Email = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    order = db.relationship("Order", backref="customer", lazy=True)

    def __repr__():
        pass


reviews = db.Table("reviews",
                   db.Column("customer_id", db.Integer, db.ForeignKey("customer.id"), primary_key=True),
                   db.Column("vendor_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
                   db.Column("review_id", db.Integer, db.ForeignKey("review.id"), primary_key=True)
                   )


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False, default=0)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100))


class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(20), nullable=False, unique=True)
    company_number = db.Column(db.Integer, unique=True, nullable=False)
    product = db.relationship("Product", backref="vendor", lazy=True)
    sales = db.relationship("Sales", backref="sales", lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100), default="No description")
    image_url = db.Column(db.String(50), default="default.jpg")
    restaurant_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    category = db.relationship("Category", secondary="categories", lazy="subquery",
                               backref=db.backref("item", lazy=True))
    review = db.relationship("Review", secondary=reviews, lazy="subquery",
                             backref=db.backref("review", lazy=True))


categories = db.Table("categories",
                      db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
                      db.Column("category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True)
                      )


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sales = db.relationship("Sales", backref="sale", lazy=True)
    consumer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))
    quantity = db.Column(db.Integer, nullable=False)
    product = db.relationship("Product", backref="product", lazy=True)
