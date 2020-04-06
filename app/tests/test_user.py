# import os
# import unittest
# import tempfile
# import json

# from flask import Flask
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from .. import create_app, db, app
# from ..users.resources.user import UserRegister, UserLogin, UserConfirm, UserLogout
# from ..models.user import UserModel
# from ..users import usersApp

# class TestCase(unittest.TestCase):

#     def setUp(self):
#         app = create_app('test')
#         self.client = app.test_client()
#         with app.app_context():
#             db.drop_all()
#             db.create_all()

#     def register(self, username, email, password):
#         return self.client.post(
#             '/users/register',
#             data=json.dumps(dict(username= username, email= email, password= password)),
#             content_type='application/json'
#         )

#     def login(self, username, password):
#         return self.client.post(
#             '/users/login',
#             data=json.dumps(dict(username=username, password=password)),
#             content_type='application/json'
#         )

#     def confirm(self):
#         return self.client.get(
#             '/users/confirm/1',
#         )

#     def test_user_register(self):
#         response = self.register('richard', 'richardkhonan0797@gmail.com', '123123')
#         self.assertEqual(response.status_code, 201)
#         self.assertIn(b'Account created successfully, a confirmation link has been sent to your email.', response.data)

#         # response = self.login('richard', '123123')
#         # self.assertEqual(response.status_code, 400)
#         # self.assertIn(b'You have not activated your account, please check your email <richardkhonan0797@gmail.com>.', response.data)

#     def test_user_confirm(self):
#         response = self.confirm()
#         self.assertEqual(response.status_code, 200)

#     def test_fail_login(self):
#         response = self.login('richard', '123123')
#         print(response.data)
#         self.assertEqual(response.status_code, 400)
#         self.assertIn(b'You have not activated your account, please check your email <{richardkhonan0797@gmail.com}>.', response.data)

#     def tearDown(self):
#         pass


# suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
# unittest.TextTestRunner(verbosity=2).run(suite)

import pytest
import json
from .. import db, create_app

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('test')
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    yield db 

def test_register(test_client):
    response = test_client.post(
            '/users/register',
            data=json.dumps(dict(username= 'richard', email= 'email@mail.com', password='123123')),
            content_type='application/json'
        )
    assert response.status_code == 201
    assert b'Account created successfully, a confirmation link has been sent to your email.' in response.data

def test_fail_login(test_client):
    response = test_client.post(
            '/users/login',
            data=json.dumps(dict(username='richard', password='123123')),
            content_type='application/json'
        )
    assert response.status_code == 400
    assert b'{"message": "You have not activated your account, please check your email <email@mail.com>."}\n' in response.data

def test_confirm(test_client):
    response = test_client.get(
        '/users/confirm/1'
    )
    assert response.status_code == 200

def test_login(test_client):
    response = test_client.post(
        '/users/login',
        data=json.dumps(dict(username='richard', password='123123')),
        content_type='application/json'
    )
    data = json.loads(response.data) 
    assert response.status_code == 200
    assert data["access_token"] is not ""
    assert data["refresh_token"] is not ""
    db.drop_all()
