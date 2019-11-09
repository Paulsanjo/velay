from marshmallow import Schema, fields, post_load, pre_load
from . import bcrypt
from .utils import upload


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
        data["image_url"] = upload(data["image_url"])
        return data


class ReviewSchema(Schema):
    rating = fields.Integer(required=True, default=3)
    title = fields.Str(required=True)
    content = fields.Str()
    restaurant = fields.Nested("VendorSchema",
                               exclude=("password", "reviews"))


class VendorSchema(Schema):
    name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    location = fields.Str(required=True)
    Email = fields.Email(required=True)
    company_number = fields.Integer(required=True)
    products = fields.Nested(ProductSchema, many=True)
    reviews = fields.Nested(ReviewSchema, many=True,
                            only=("name", "price", "description"))

    @post_load
    def hash_password(self, data, **kwargs):
        data["password"] = bcrypt.generate_password_hash(data["password"])
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

    date = fields.DateTime(required=True)
    orders = fields.Nested("OrderSchema", many=True)
    vendors = fields.Nested("VendorSchema",
                            only=("name", "Email"))

    class Meta:
        fields = ("orders", "date", "vendors")


class CustomerSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    Address = fields.Str()
    Email = fields.Email(required=True)
    phone_number = fields.Integer(required=True,
                                  error_messages={
                                      "phone number": "not a valid phone number"
                                  })
    orders = fields.Nested(OrderSchema)

    @post_load
    def hash_password(self, data, **kwargs):
        data["password"] = bcrypt.generate_password_hash(data["password"])
        return data
