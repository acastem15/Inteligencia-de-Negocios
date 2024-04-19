from flask import Flask
import os

def create_app(config_name):
    app = Flask(__name__)
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@192.168.112.5:5432/offer-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app