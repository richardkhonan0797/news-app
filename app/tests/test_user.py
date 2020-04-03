import os
import unittest
import tempfile

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .. import create_app, db
from ..users.resources.user import UserRegister
from ..models.user import UserModel


class TestCase(unittest.TestCase):

    def setUp(self):
        app = create_app('test')
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        pass

    def register(self, username, email, password):
        return self.client.post(
            '/register',
            data=dict(username=username, email=email, password=password),
        )

    def test_user_registration(self):
        response = self.register('richard', 'richardkhonan0797@gmail.com', '123123')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Account created successfully, a confirmation link has been sent to your email.', response.data.message)

if __name__ == '__main__':
    unittest.main()