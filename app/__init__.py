import os

from flask import Flask

from config import apply_config

app = Flask(__name__)

app.config.from_object(apply_config(os.environ.get('FLASK_ENV')))

from app import routes
