import os
from os.path import join, dirname

from pampy import match, _
from dotenv import load_dotenv


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sample-key')


class DevelopmentConfig(Config):
    FLASK_DEBUG = 1


class ProductionConfig(Config):
    FLASK_DEBUG = 0


def apply_config(env):
    return match(env,
                 'production', ProductionConfig(),
                 'development', DevelopmentConfig(),
                 'staging', DevelopmentConfig(),
                 _, DevelopmentConfig())