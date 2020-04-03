import os

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('..') / '.env'

load_dotenv(dotenv_path=env_path)

class DevelopmentConfiguration(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI', 'sqlite:///news-app.db')
    PROPAGATE_EXCEPTION = True
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

class TestConfiguration(object):
    TESTING = True
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    PROPAGATE_EXCEPTION = True
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


app_config = {
    'development': DevelopmentConfiguration,
    'test': TestConfiguration
}