import os
from urllib.parse import quote_plus

debug_mode = True

class Config():
    APP_PATH = os.path.dirname(__file__)
    DEBUG = debug_mode

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }

class DevelopmentConfig(Config):
    DEBUG = debug_mode
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DB_NAME = os.getenv('POSTGRES_NAME', 'localserv')
    DB_USER = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASS = os.getenv('POSTGRES_PASSWORD', quote_plus('postgres'))
    DB_SERVICE = os.getenv('POSTGRES_SERVICE', 'localhost')
    DB_PORT = os.getenv('POSTGRES_PORT', '5432')
    COMMON_DATABASE_PATH = f'postgresql://{DB_USER}:{DB_PASS}@{DB_SERVICE}:{DB_PORT}'

    SQLALCHEMY_DATABASE_URI = f'{COMMON_DATABASE_PATH}/{DB_NAME}'


class ProductionConfig(Config):
    DEBUG = debug_mode
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DB_NAME = os.getenv('POSTGRES_NAME', 'localserv')
    DB_USER = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASS = os.getenv('POSTGRES_PASSWORD', quote_plus('postgres'))
    DB_SERVICE = os.getenv('POSTGRES_SERVICE', 'localhost')
    DB_PORT = os.getenv('POSTGRES_PORT', '5432')
    COMMON_DATABASE_PATH = f'postgresql://{DB_USER}:{DB_PASS}@{DB_SERVICE}:{DB_PORT}'

    SQLALCHEMY_DATABASE_URI = f'{COMMON_DATABASE_PATH}/{DB_NAME}'


config = ProductionConfig if not debug_mode else DevelopmentConfig