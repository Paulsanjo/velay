import unittest
from tests.base import BaseTestCase


class TestCase(BaseTestCase):
    def test_home_route(self):
        response = self.client.get('/', content_type="application/json")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
