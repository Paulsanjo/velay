from core import app
from core.config import TestConfig
from flask_testing import TestCase
# from core.models import User, BlogPost


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass
