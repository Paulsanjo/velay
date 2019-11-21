import json
import unittest
from flask import request
from tests.base import BaseTestCase


class ConsumerTestCase(BaseTestCase):

    def test_user_registration(self):
        data = dict(first_name='david', last_name='afolabi',
                    password='#Trending32fm', Address='12, Kurumi, Ibadan, Nigeria',
                    Email='uzezio22@gmail.com',
                    phone_number='09069038781')
        response = self.client.post("/register/user",
                                    data=json.dumps(data))
        # self.assertIn(b'message', response.data)
        self.assertIn("/register/user", request.url)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
