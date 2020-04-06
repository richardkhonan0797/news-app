from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail
from .config import app_config

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()
blacklist = set()
app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    jwt = JWTManager(app)

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
        
    from .users import usersApp
    from .news import news_app

    app.register_blueprint(usersApp, url_prefix='/users')
    app.register_blueprint(news_app, url_prefix='/news')

    @app.before_first_request
    def create_tables():
        db.create_all()

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist

    return app