from flask import Blueprint
from flask_restful import Api
from .routes import initialize_routes

news_app = Blueprint('news', __name__)
news_app_api = Api(news_app)
initialize_routes(news_app_api)