import os
from dotenv import load_dotenv

load_dotenv()
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # secert key for development purposes, choose different key in production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # log slow database queries
    SQLALCHEMY_RECORD_QUERIES = os.environ.get('SQLALCHEMY_RECORD_QUERIES', '0').lower() in ['true', '1']
    SLOW_DB_QUERY_TIME = 0.5
    # mail configurations
    MAIL_SUBJECT_PREFIX = ''
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or '25')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', '1').lower() in ['true', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SENDER = os.environ.get('MAIL_SENDER')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'a_random_string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        # add logging
        pass


cfg_options = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
