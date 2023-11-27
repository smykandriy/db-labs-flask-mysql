import logging
import secrets
from typing import Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from amusement_park.auth.route import register_routes


SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

db = SQLAlchemy()


def create_app(app_config: dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :return: Flask application object
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}  # type: ignore

    _init_db(app)
    register_routes(app)

    return app


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import amusement_park.auth.domain

    with app.app_context():
        db.create_all()
