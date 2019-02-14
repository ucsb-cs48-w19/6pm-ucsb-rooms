import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-the_secret_key!WhereIsEvery1?'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # #SECRET_KEY = 'this-really-needs-to-be-changed'
    # Uncomment this to enable database connection.
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  'sqlite:///site.db'
    print("Database URL configured as:", SQLALCHEMY_DATABASE_URI)

    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
