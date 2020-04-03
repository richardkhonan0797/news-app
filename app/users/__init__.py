from flask import Blueprint
from flask_restful import Api
from .routes import initialize_routes

usersApp = Blueprint('users', __name__)
api_users_app = Api(usersApp)
initialize_routes(api_users_app)
