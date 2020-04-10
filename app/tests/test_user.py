import pytest
import json
from . import flask_app
from .. import db
from ..models.user import UserModel
from ..schemas.user import UserSchema

user_schema = UserSchema()

@pytest.fixture(scope='module')
def test_client():
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    db.drop_all()
    db.create_all()
    yield testing_client
    ctx.pop()

# @pytest.fixture(scope='module')
# def init_database():
#     db.create_all()
#     yield db 

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
    user = UserModel.find_by_id('1')
    user_data = user_schema.dump(user)
    hash_val = user_data['hash_val']
    response = test_client.get(
        '/users/confirm/{}'.format(hash_val)
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
    assert data["access_token"] != ""
    assert data["refresh_token"] != ""
    db.drop_all()
