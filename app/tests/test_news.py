import pytest
import json

from .. import create_app, db
from ..models.user import UserModel
from ..models.news import NewsModel

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('test')
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
    test_client.get('/users/confirm/1')
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
