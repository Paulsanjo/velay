from marshmallow import (Schema, fields, post_load, pre_load,
                         validate)
from . import bcrypt
from .utils import Tools


class CategorySchema(Schema):
    name = fields.Str(required=True)


class ProductSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Integer(required=True)
    quantity = fields.Str(required=True)
    description = fields.Str()
    image_url = fields.Str()
    category = fields.Nested(CategorySchema, many=True)
    orders = fields.Nested("OrderSchema",
                           many=True, exclude=("product",))
    restaurant = fields.Nested("VendorSchema",
                               many=True, exclude=("product",
                                                   "password"))

    class Meta:
        fields = ("name", "price", "quantity",
                  "description", "image_url",
                  "category", "orders", "vendors")

    @pre_load
    def iamge(self, data, **kwargs):
        data["image_url"] = Tools.upload(data["image_url"])
        return data


class ReviewSchema(Schema):
    rating = fields.Integer(required=True, default=3,
                            validate=validate.Length(min=1, max=5))
    title = fields.Str(required=True)
    content = fields.Str()
    restaurant = fields.Nested("VendorSchema",
                               exclude=("password", "reviews"))


class VendorSchema(Schema, Tools):
    name = fields.Method("setup", deserialize="load_name",
                         required=True, validate=validate.Length(min=3, max=20))
    password = fields.Str(required=True, load_only=True,
                          validate=validate.Length(min=8, max=15))
    location = fields.Str(required=True)
    Email = fields.Email(required=True)
    company_number = fields.Integer(required=True, validate=Tools.contact)
    products = fields.Nested(ProductSchema, many=True)
    reviews = fields.Nested(ReviewSchema, many=True,
                            only=("name", "price", "description"))

    @post_load
    def adjust_data(self, data, **kwargs):
        data["password"] = bcrypt.generate_password_hash(data["password"].strip())
        data["phone_number"] = int(data["phone_number"])
        return data


class OrderSchema(Schema):
    quantity = fields.Integer(required=True, default=1)
    product = fields.Nested("ProductSchema",
                            exclude=("orders",))

    class Meta:
        fields = ("product", "quantity")


class SaleSchema(Schema):
    """VendorSchema is within quotations here if written like this is can refer
    to a Schema that is yet to be created, if outside quotations then schema should already be
    defined before the schema that calls it."""

    orders = fields.Nested("OrderSchema", many=True)
    vendors = fields.Nested("VendorSchema",
                            only=("name", "Email"))

    class Meta:
        fields = ("orders", "date", "vendors")


class CustomerSchema(Schema, Tools):
    first_name = fields.Method("setup", deserialize="load_name",
                               required=True, validate=validate.Length(min=3, max=20))
    last_name = fields.Method("setup", deserialize="load_name",
                              required=True, validate=validate.Length(min=3, max=20))
    password = fields.Str(required=True, load_only=True,
                          validate=validate.Length(min=8, max=15))
    Address = fields.Str()
    Email = fields.Email(required=True, validate=validate.Email())
    phone_number = fields.Integer(required=True, validate=Tools.contact)
    orders = fields.Nested(OrderSchema)

    @post_load
    def adjust_data(self, data, **kwargs):
        data["password"] = bcrypt.generate_password_hash(data["password"].strip())
        data["phone_number"] = int(data["phone_number"])
        return data
