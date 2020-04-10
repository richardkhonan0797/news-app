import pytest
import json

from .. import db
from . import flask_app
from ..models.user import UserModel
from ..models.news import NewsModel
from ..schemas.user import UserSchema

user_schema = UserSchema()

@pytest.fixture(scope='module')
def test_client():
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    db.drop_all()
    db.create_all()

    user = UserModel(
        username = 'richard', 
        email = 'email@mail.com', 
        password = '123123'
    )
    news = [NewsModel(
        source_id = 'test',
        source_name = 'test',
        author = 'test',
        title = 'test',
        description = 'test',
        url = 'test',
        urlToImage = 'test',
        publishedAt = 'test',
        content = 'test',
        country = 'test',
        category = 'test',
    )]
    user.save_to_db()
    NewsModel.save_all_to_db(news)
    yield testing_client
    ctx.pop()

def test_news(test_client):
    user = UserModel.find_by_id('1')
    u_data = user_schema.dump(user)
    hash_val = u_data['hash_val']
    test_client.get('/users/confirm/{}'.format(hash_val))
    user = test_client.post(
            '/users/login',
            data = json.dumps(dict(username='richard', password='123123')),
            content_type='application/json'
        )
    user_data = json.loads(user.data)

    access_token = 'Bearer {}'.format(user_data['access_token'])

    news = test_client.get(
        '/news/test/test',
        headers={'Authorization': access_token},
        content_type='application/json'
    )
    news_data = json.loads(news.data.decode('utf-8'))
    print(news_data)

    assert news.status_code == 200
    assert news_data[0]['source_id'] == 'test'
    assert news_data[0]['source_name'] == 'test'
