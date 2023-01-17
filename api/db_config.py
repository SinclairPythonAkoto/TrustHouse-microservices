from flask_sqlalchemy import SQLAlchemy
from .config import DATABASE_CONNECTION_STRING

db = SQLAlchemy()

def configure_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_STRING
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
