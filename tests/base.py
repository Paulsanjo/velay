from core import app, db
from core.config import TestConfig
from flask_testing import TestCase
from core.models import (Customer, Review, Vendor,
                         Product, Sales, Order)


class BaseTestCase(TestCase):
    """A base test case setup."""

    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Customer(first_name="kome", last_name="ijanusi",
                                password="#dannyBoy34", Address="Bendel Estate",
                                Email="kome@gmail.com",
                                phone_number="0809312998"))
        # db.session.add(Vendor())
        db.session.add(Product(name='sneakers', price=300, quantity=100,
                               description='chocolate bar'))
        # db.session.add(Review())
        # db.session.add()
        # db.session.add()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
