import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    HASH_CHECK = os.environ['HASH_CHECK']
    BCRYPT_LOG_ROUNDS = 12
    CSRF_ENABLED = True
    SECRET_KEY = 'c2zaLiRQEhOb'

class Production(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG =True

class TestingConfig(Config):
    TESTING = True